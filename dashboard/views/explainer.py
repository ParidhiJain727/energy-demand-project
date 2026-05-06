import streamlit as st

def render_explainer_page():
    st.markdown("""
    <style>
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .explainer-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
        justify-content: space-between;
        padding: 20px 0;
    }
    .explainer-card {
        flex: 1 1 calc(50% - 25px);
        min-width: 300px;
        border: 4px solid #000;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 8px 8px 0px #000;
        display: flex;
        flex-direction: column;
        opacity: 0;
        transform: translateY(30px);
        animation: fadeInUp 0.8s ease-out forwards;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
        background-color: white;
    }
    .explainer-card:hover {
        transform: translate(-4px, -4px) !important;
        box-shadow: 12px 12px 0px #000;
    }
    
    /* Animated SVG Icons */
    .svg-icon {
        width: 60px;
        height: 60px;
        margin-bottom: 20px;
    }
    .clock-hand {
        transform-origin: center;
        animation: rotate 10s linear infinite;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .pulse-arrow {
        animation: arrowMove 1.5s ease-in-out infinite;
    }
    @keyframes arrowMove { 0% { transform: translateX(0); } 50% { transform: translateX(10px); } 100% { transform: translateX(0); } }
    
    .wave-path {
        animation: waveMove 3s linear infinite;
    }
    @keyframes waveMove { 0% { transform: translateX(0); } 100% { transform: translateX(-40px); } }

    .card-title {
        font-size: 24px;
        font-weight: 900;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .card-desc {
        font-size: 14px;
        line-height: 1.6;
        flex-grow: 1;
    }
    
    /* Hero Section Enhancements */
    .hero-section {
        position: relative;
        text-align: center;
        padding: 60px 20px;
        background: #ffffff;
        color: #000000;
        border-radius: 15px;
        border: 4px solid #000;
        box-shadow: 10px 10px 0px #cce0ff;
        margin-bottom: 40px;
        animation: fadeInUp 0.6s ease-out;
        overflow: hidden;
        cursor: crosshair;
        transition: box-shadow 0.3s ease;
    }
    
    .hero-section:hover {
        box-shadow: 15px 15px 0px #ffd6e0;
    }

    /* Interactive Electricity Grid */
    .hero-wave-container {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
        opacity: 0.4;
        transition: opacity 0.3s ease;
    }
    
    .hero-section:hover .hero-wave-container {
        opacity: 0.8;
    }
    
    .grid-line {
        fill: none;
        stroke: #cce0ff; /* Pastel Blue */
        stroke-width: 3;
        stroke-dasharray: 15, 15;
        animation: flowLine 15s linear infinite;
        transition: stroke 0.3s ease, animation-duration 0.3s ease;
    }
    
    .grid-power {
        fill: none;
        stroke: #ffd6e0; /* Pastel Red */
        stroke-width: 4;
        stroke-dasharray: 20, 10;
        animation: flowLine 8s linear infinite reverse;
        transition: stroke 0.3s ease, animation-duration 0.3s ease;
    }
    
    .grid-node {
        fill: #000000;
        animation: pulseNode 2s infinite alternate;
        transition: fill 0.3s ease;
    }

    .hero-section:hover .grid-line {
        stroke: #000000;
        animation-duration: 4s;
    }

    .hero-section:hover .grid-power {
        stroke: #000000;
        stroke-width: 5;
        animation-duration: 2s;
    }
    
    .hero-section:hover .grid-node {
        fill: #ffd6e0;
        animation-duration: 0.5s;
    }

    @keyframes flowLine {
        from { stroke-dashoffset: 1000; }
        to { stroke-dashoffset: 0; }
    }
    
    @keyframes pulseNode {
        0% { r: 3; opacity: 0.5; }
        100% { r: 6; opacity: 1; }
    }

    .hero-content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border: 4px solid #000;
        border-radius: 15px;
        display: inline-block;
        max-width: 900px;
        box-shadow: 8px 8px 0px #cce0ff;
        transition: box-shadow 0.3s ease;
    }
    
    .hero-section:hover .hero-content {
        box-shadow: 12px 12px 0px #ffd6e0;
    }
    
    /* Colors and pure CSS stagger delays */
    .card-1 { background-color: #ffd6e0; animation-delay: 0.2s; }
    .card-2 { background-color: #bdfcc9; animation-delay: 0.4s; }
    .card-3 { background-color: #cce0ff; animation-delay: 0.6s; }
    .card-4 { background-color: #fff0b3; animation-delay: 0.8s; }
    </style>
    """, unsafe_allow_html=True)

    hero_html = """
    <div class="hero-section">
        <div class="hero-wave-container">
            <svg width="100%" height="100%" viewBox="0 0 1000 200" preserveAspectRatio="xMidYMid slice">
                <!-- Circuit / Grid Lines -->
                <path class="grid-line" d="M-50,40 H150 V140 H350 V60 H550 V160 H750 V80 H950 V120 H1050" />
                <path class="grid-line" d="M-50,160 H100 V80 H300 V180 H500 V40 H700 V140 H900 V60 H1050" />
                <path class="grid-power" d="M-50,100 H200 V40 H400 V120 H600 V80 H800 V160 H1050" />
                
                <!-- Intersections / Nodes -->
                <circle class="grid-node" cx="150" cy="40" r="4" />
                <circle class="grid-node" cx="150" cy="140" r="4" />
                <circle class="grid-node" cx="350" cy="140" r="4" />
                <circle class="grid-node" cx="350" cy="60" r="4" />
                <circle class="grid-node" cx="550" cy="60" r="4" />
                <circle class="grid-node" cx="550" cy="160" r="4" />
                <circle class="grid-node" cx="750" cy="160" r="4" />
                <circle class="grid-node" cx="750" cy="80" r="4" />
                <circle class="grid-node" cx="950" cy="80" r="4" />
                <circle class="grid-node" cx="950" cy="120" r="4" />
                
                <circle class="grid-node" cx="100" cy="160" r="4" />
                <circle class="grid-node" cx="100" cy="80" r="4" />
                <circle class="grid-node" cx="300" cy="80" r="4" />
                <circle class="grid-node" cx="300" cy="180" r="4" />
                <circle class="grid-node" cx="500" cy="180" r="4" />
                <circle class="grid-node" cx="500" cy="40" r="4" />
                <circle class="grid-node" cx="700" cy="40" r="4" />
                <circle class="grid-node" cx="700" cy="140" r="4" />
                <circle class="grid-node" cx="900" cy="140" r="4" />
                <circle class="grid-node" cx="900" cy="60" r="4" />
                
                <circle class="grid-node" cx="200" cy="100" r="5" />
                <circle class="grid-node" cx="200" cy="40" r="5" />
                <circle class="grid-node" cx="400" cy="40" r="5" />
                <circle class="grid-node" cx="400" cy="120" r="5" />
                <circle class="grid-node" cx="600" cy="120" r="5" />
                <circle class="grid-node" cx="600" cy="80" r="5" />
                <circle class="grid-node" cx="800" cy="80" r="5" />
                <circle class="grid-node" cx="800" cy="160" r="5" />
            </svg>
        </div>
        <div class="hero-content">
            <h1 style='color: #000000 !important; margin: 0; font-size: 3rem; text-shadow: 4px 4px 0px #ffd6e0;'>POWER PLAY</h1>
            <p style='color: #000000 !important; font-weight: bold; margin-top: 10px; font-size: 1.2rem; letter-spacing: 2px; background: #cce0ff; display: inline-block; padding: 5px 15px; border: 2px solid #000; border-radius: 8px;'>DECODING THIS AI-DRIVEN DEMAND FORECASTER</p>
            <p style='color: #000000 !important; margin-top: 20px; font-size: 1.1rem; line-height: 1.6; font-weight: bold;'>
                This forecasting engine utilizes an optimized <b>Extreme Gradient Boosting (XGBoost)</b> architecture to synthesize complex autoregressive patterns and seasonal dependencies. By cross-referencing multi-scale historical lags with rolling statistical benchmarks, the system provides high-precision energy demand projections to stabilize grid operations and optimize resource allocation.
            </p>
        </div>
    </div>
    """
    st.markdown(hero_html.replace('\n', ''), unsafe_allow_html=True)

    overview_html = """
    <div class="explainer-container">
        <!-- XGBoost Card -->
        <div class="explainer-card" style="background-color: #e0f0ff; flex: 1 1 calc(50% - 25px); animation-delay: 0.1s;">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                <path d="M4 4h16v16H4z"/>
                <path d="M12 4v16M4 12h16"/>
                <circle cx="12" cy="12" r="3" fill="#000"/>
            </svg>
            <div class="card-title" style="font-size: 2rem;">THE XGBOOST ENGINE</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Extreme Gradient Boosting</strong><br><br>
                XGBoost is a decision-tree-based ensemble algorithm designed for speed and predictive accuracy. It works by building a sequence of models where each new iteration specifically targets the errors made by previous ones. This makes it exceptionally effective at identifying complex, non-linear relationships in tabular energy data that traditional models often fail to capture.
            </div>
        </div>
        <!-- Benefits Card -->
        <div class="explainer-card" style="background-color: #f0e0ff; flex: 1 1 calc(50% - 25px); animation-delay: 0.2s;">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
            </svg>
            <div class="card-title" style="font-size: 2rem;">HOW IT BENEFITS YOU</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Grid Stability and Efficiency</strong><br><br>
                Accurate demand forecasting is essential for maintaining a stable electrical grid. By predicting peak usage periods, utility providers can optimize power generation and reduce reliance on expensive, high-emission backup plants. This leads to more efficient resource management, a more resilient infrastructure, and lower long-term operational costs for both providers and consumers.
            </div>
        </div>
    </div>
    """
    st.markdown(overview_html.replace('\n', ''), unsafe_allow_html=True)

    st.markdown("<br><h3 style='text-align: center; border-bottom: 4px solid #000; padding-bottom: 10px;'>THE FEATURES (HOW IT THINKS)</h3>", unsafe_allow_html=True)
    
    cards_html = """
    <div class="explainer-container">
        <!-- Card 1 -->
        <div class="explainer-card card-1">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <line class="clock-hand" x1="12" y1="12" x2="12" y2="6" stroke-linecap="round"/>
                <line x1="12" y1="12" x2="16" y2="12" stroke-linecap="round"/>
            </svg>
            <div class="card-title" style="font-size: 2rem;">TEMPORAL DNA</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Hour, Day, Month, Weekend</strong><br><br>
                Energy consumption follows predictable human routines. By tracking the <b>Hour of Day</b> and <b>Day of Week</b>, the model accounts for recurring cycles like the morning rush and evening peaks. Identifying weekends and holidays further refines these patterns, allowing the system to categorize each moment based on historical residential and commercial habits.
            </div>
        </div>
        <!-- Card 2 -->
        <div class="explainer-card card-2">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2" stroke-dasharray="2 2"/>
                <path class="pulse-arrow" d="M2 12H16M16 12L12 8M16 12L12 16" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div class="card-title" style="font-size: 2rem;">LAG 24 (The Daily Echo)</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Energy Demand 24 Hours Ago</strong><br><br>
                Electricity demand is highly autoregressive, meaning yesterday’s consumption is a primary indicator for today. By analyzing data from exactly 24 hours ago, the model establishes a reliable baseline for the "Standard Load" of the city. This helps the system anticipate recurring daily habits that simple time-tracking might otherwise overlook.
            </div>
        </div>
        <!-- Card 3 -->
        <div class="explainer-card card-3">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                <path class="pulse-arrow" d="M22 12H8M8 12L12 8M8 12L12 16" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="4" cy="12" r="2" fill="black"/>
            </svg>
            <div class="card-title" style="font-size: 2rem;">LAG 1 (The Pulse)</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Energy Demand 1 Hour Ago</strong><br><br>
                Demand typically changes gradually rather than instantaneously. By incorporating usage data from the previous hour, the model captures current <b>Momentum</b>. This serves as a critical correction factor, allowing the system to remain responsive to short-term fluctuations and determine whether the grid is currently in an upward surge or a cooling phase.
            </div>
        </div>
        <!-- Card 4 -->
        <div class="explainer-card card-4">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" style="overflow: hidden;">
                <path class="wave-path" d="M-40 12 Q-20 4 0 12 T40 12 T80 12 T120 12" />
            </svg>
            <div class="card-title" style="font-size: 2rem;">ROLLING STATS</div>
            <div class="card-desc" style="font-size: 1.25rem;">
                <strong style="font-size: 1.2em;">Rolling Mean & Standard Deviation</strong><br><br>
                Raw energy data is often volatile. The <b>Rolling Mean</b> acts as a smoothing filter to highlight the true underlying trend of the day. Meanwhile, the <b>Rolling Standard Deviation</b> measures volatility, helping the model distinguish between minor data anomalies and genuine shifts in consumption patterns that require a forecast adjustment.
            </div>
        </div>
    </div>
    """
    st.markdown(cards_html.replace('\n', ''), unsafe_allow_html=True)
