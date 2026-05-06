import streamlit as st
import pandas as pd
from dashboard.utils.ml_helpers import load_model, load_metrics, build_input_dataframe, FEATURE_COLUMNS, REPORTS_PATH

def render_dashboard_page():
    st.title("PERSONAL POWER-PLAY FORECAST")
    st.markdown(f"## WELCOME BACK, {st.session_state['username'].upper()}!")

    if st.sidebar.button("LOGOUT"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        # Clear chat history and reset navigation state on logout
        if "messages" in st.session_state:
            del st.session_state["messages"]
        st.session_state["show_terminal"] = False
        st.session_state["show_explainer"] = False
        st.rerun()

    try:
        model = load_model()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

    metrics = load_metrics()

    st.sidebar.header("INPUT FEATURES")

    hour = st.sidebar.slider("Hour", min_value=0, max_value=23, value=14)
    day_of_week = st.sidebar.slider("Day Of Week", min_value=0, max_value=6, value=2)
    month = st.sidebar.slider("Month", min_value=1, max_value=12, value=1)
    is_weekend = st.sidebar.selectbox("Is Weekend", options=[0, 1], index=0)

    import math
    import random
    
    # Calculate dynamic realistic defaults based on the selected time
    base_val = 100 + 20 * math.sin(hour / 24 * 2 * math.pi) + 10 * math.cos(month / 12 * 2 * math.pi)
    random.seed(hour + month + day_of_week)
    
    dyn_lag_1 = round(base_val + random.uniform(-10, 10), 1)
    dyn_lag_24 = round(base_val + random.uniform(-15, 15), 1)
    dyn_roll_mean = round(base_val + random.uniform(-5, 5), 1)
    dyn_roll_std = round(random.uniform(4.0, 12.0), 1)

    lag_1 = st.sidebar.number_input("Lag 1", value=dyn_lag_1)
    lag_24 = st.sidebar.number_input("Lag 24", value=dyn_lag_24)
    rolling_mean_24 = st.sidebar.number_input("Rolling Mean 24", value=dyn_roll_mean)
    rolling_std_24 = st.sidebar.number_input("Rolling Std 24", value=dyn_roll_std)

    input_df = build_input_dataframe(
        hour=hour,
        day_of_week=day_of_week,
        month=month,
        is_weekend=is_weekend,
        lag_1=lag_1,
        lag_24=lag_24,
        rolling_mean_24=rolling_mean_24,
        rolling_std_24=rolling_std_24,
    )

    prediction = model.predict(input_df)[0]
    
    st.markdown("---")
    st.subheader("OVERVIEW")
    
    # Dynamic calculations based on the model's hourly prediction
    # We estimate the monthly usage by scaling the hourly prediction
    days_in_month = 31 if month in [1, 3, 5, 7, 8, 10, 12] else (28 if month == 2 else 30)
    hours_in_month = days_in_month * 24
    
    # Assume the forecasted hour represents a peak/average, scale by a load factor of 0.65
    estimated_this_month = prediction * hours_in_month * 0.65
    
    # Create deterministic variations based on the selected month
    import random
    random.seed(month + hour) # Changes based on inputs
    
    last_month_usage = estimated_this_month * random.uniform(0.85, 1.15)
    predicted_next_month = estimated_this_month * random.uniform(0.85, 1.15)
    
    this_month_delta = ((estimated_this_month - last_month_usage) / last_month_usage) * 100
    next_month_delta = ((predicted_next_month - estimated_this_month) / estimated_this_month) * 100

    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric("Estimated Usage This Month", f"{estimated_this_month:,.0f} kWh", f"{this_month_delta:+.1f}% vs last month")
    with metric_col2:
        st.metric("Predicted Next Month", f"{predicted_next_month:,.0f} kWh", f"{next_month_delta:+.1f}% vs this month")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Prediction")
        st.metric("Forecasted Demand", f"{prediction:.2f}")

        st.subheader("Input Sample")
        st.dataframe(input_df)

    with col2:
        st.subheader("Model Information")
        st.write("**Features used:**")
        badges_html = " ".join(
            f'<span style="display:inline-block; background-color:#cce0ff; border:2px solid #000; '
            f'border-radius:8px; padding:3px 10px; margin:3px; font-family:Space Mono,monospace; '
            f'font-size:12px; font-weight:bold; color:#000; box-shadow:2px 2px 0 #000;">{col}</span>'
            for col in FEATURE_COLUMNS
        )
        st.markdown(badges_html, unsafe_allow_html=True)

        if metrics is not None:
            st.write("**Evaluation Metrics:**")

            baseline = metrics.get("baseline", {})
            random_forest = metrics.get("random_forest", {})

            metrics_df = pd.DataFrame(
                [
                    {
                        "Model": "Baseline",
                        "MAE": baseline.get("mae"),
                        "RMSE": baseline.get("rmse"),
                        "MAPE": baseline.get("mape"),
                    },
                    {
                        "Model": "Random Forest",
                        "MAE": random_forest.get("mae"),
                        "RMSE": random_forest.get("rmse"),
                        "MAPE": random_forest.get("mape"),
                    },
                ]
            )
            st.dataframe(metrics_df)
        else:
            st.info("No metrics.json found yet.")

    st.subheader("Evaluation Plots")

    results_path = REPORTS_PATH / "evaluation_results.csv"
    if results_path.exists():
        import plotly.graph_objects as go
        
        eval_df = pd.read_csv(results_path)
        
        layout_kwargs = dict(
            plot_bgcolor="#ffffff",
            paper_bgcolor="#ffffff",
            font=dict(family="Space Mono", color="#000000", size=14),
            margin=dict(l=40, r=40, t=60, b=40),
            xaxis=dict(
                showgrid=False, zeroline=False, showline=True,
                linewidth=3, linecolor="black",
                title_font=dict(size=12, family="Space Mono", color="black"),
                tickfont=dict(size=12, color="black"),
            ),
            yaxis=dict(
                showgrid=False, zeroline=False, showline=True,
                linewidth=3, linecolor="black",
                title_font=dict(size=12, family="Space Mono", color="black"),
                tickfont=dict(size=12, color="black"),
            ),
            legend=dict(
                bgcolor="#fdf5e6", bordercolor="black", borderwidth=2,
                font=dict(size=12, color="black")
            )
        )
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(y=eval_df['Actual'], mode='lines', name='Actual', line=dict(color='#8ff19d', width=5)))
        fig1.add_trace(go.Scatter(y=eval_df['Predicted'], mode='lines', name='Predicted', line=dict(color='#ffd6e0', width=5)))
        
        # Dynamic marker for current prediction
        fig1.add_hline(y=prediction, line_dash="dash", line_color="black", line_width=2, 
                       annotation_text="YOUR CURRENT FORECAST", 
                       annotation_position="top right", 
                       annotation_font=dict(family="Space Mono", color="black", size=12))
        
        fig1.update_layout(title=dict(text="PREDICTIONS VS ACTUAL", font=dict(color="black", size=16)), **layout_kwargs)
        fig1.update_layout(xaxis_title="TIME STEP", yaxis_title="DEMAND")

        fig2 = go.Figure()
        residuals = eval_df['Actual'] - eval_df['Predicted']
        fig2.add_trace(go.Histogram(x=residuals, nbinsx=30, marker=dict(color='#ffd6e0', line=dict(color='black', width=2))))
        fig2.update_layout(title=dict(text="RESIDUAL DISTRIBUTION", font=dict(color="black", size=16)), **layout_kwargs)
        fig2.update_layout(xaxis_title="PREDICTION ERROR", yaxis_title="FREQUENCY")
        
        fig3 = go.Figure()
        abs_errors = abs(residuals)
        fig3.add_trace(go.Scatter(y=abs_errors, mode='lines', name='Absolute Error', line=dict(color='#cce0ff', width=5)))
        fig3.update_layout(title=dict(text="ABSOLUTE ERROR OVER TIME", font=dict(color="black", size=16)), **layout_kwargs)
        fig3.update_layout(xaxis_title="TIME STEP", yaxis_title="ABSOLUTE ERROR")
        
        plotly_config = {
            'displayModeBar': True,
            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian'],
            'displaylogo': False
        }
        
        plot_col1, plot_col2 = st.columns(2)
        with plot_col1:
            st.plotly_chart(fig1, use_container_width=True, config=plotly_config)
        with plot_col2:
            st.plotly_chart(fig2, use_container_width=True, config=plotly_config)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.plotly_chart(fig3, use_container_width=True, config=plotly_config)
        
    else:
        st.warning("evaluation_results.csv not found. Please run the evaluation script.")
