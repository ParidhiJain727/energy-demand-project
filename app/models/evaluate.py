import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from app.core.config import FEATURE_COLUMNS, TARGET_COLUMN
from dashboard.dashboard_app import FIGURES_PATH

BASE_DIR = Path(__file__).resolve().parents[2]

FEATURE_DATA_PATH = BASE_DIR / "data/processed/features.csv"
MODEL_PATH = BASE_DIR / "models/trained_model.pkl"
METRICS_PATH = BASE_DIR / "reports/metrics.json"

def load_data_and_model():
    if not FEATURE_DATA_PATH.exists():
        raise FileNotFoundError(f"Feature dataset not found at {FEATURE_DATA_PATH}")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")

    df = pd.read_csv(FEATURE_DATA_PATH)
    model = joblib.load(MODEL_PATH)

    return df, model

def split_test_data(df: pd.DataFrame, test_size: float = 0.2):
    split_index = int(len(df) * (1 - test_size))
    test_df = df.iloc[split_index:].copy()
    return test_df

def generate_predictions(test_df: pd.DataFrame, model):
    X_test = test_df.loc[:, FEATURE_COLUMNS]
    y_test = test_df[TARGET_COLUMN]
    predictions = model.predict(X_test)
    return y_test, predictions

def setup_plot_style(fig, ax):
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    for spine in ax.spines.values():
        spine.set_edgecolor('#000000')
        spine.set_linewidth(3)
    ax.tick_params(colors='black', width=2)
    ax.xaxis.label.set_color('black')
    ax.xaxis.label.set_fontweight('bold')
    ax.yaxis.label.set_color('black')
    ax.yaxis.label.set_fontweight('bold')
    ax.title.set_color('black')
    ax.title.set_fontweight('bold')

def plot_prediction_vs_actual(y_test, predictions):
    fig, ax = plt.subplots(figsize=(10, 5))
    setup_plot_style(fig, ax)
    
    ax.plot(y_test.values, label="Actual", color="#bdfcc9", linewidth=3)
    ax.plot(predictions, label="Predicted", color="#ffd6e0", linewidth=3)
    
    ax.set_title("PREDICTIONS VS ACTUAL")
    ax.set_xlabel("TIME STEP")
    ax.set_ylabel("DEMAND")
    ax.legend(facecolor='#fdf5e6', edgecolor='black', framealpha=1).get_frame().set_linewidth(2)
    plt.tight_layout()

    FIGURES_PATH.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURES_PATH / "prediction_vs_actual.png")
    plt.close()

def plot_residuals_distribution(y_test, predictions):
    residuals = y_test.values - predictions

    fig, ax = plt.subplots(figsize=(10, 5))
    setup_plot_style(fig, ax)
    
    ax.hist(residuals, bins=30, color="#ffd6e0", edgecolor="black", linewidth=2)
    
    ax.set_title("RESIDUAL DISTRIBUTION")
    ax.set_xlabel("PREDICTION ERROR")
    ax.set_ylabel("FREQUENCY")
    plt.tight_layout()

    plt.savefig(FIGURES_PATH / "residuals.png")
    plt.close()

def plot_error_over_time(y_test, predictions):
    absolute_errors = abs(y_test.values - predictions)

    fig, ax = plt.subplots(figsize=(10, 5))
    setup_plot_style(fig, ax)
    
    ax.plot(absolute_errors, color="#cce0ff", linewidth=3)
    
    ax.set_title("ABSOLUTE ERROR OVER TIME")
    ax.set_xlabel("TIME STEP")
    ax.set_ylabel("ABSOLUTE ERROR")
    plt.tight_layout()

    plt.savefig(FIGURES_PATH / "absolute_error_over_time.png")
    plt.close()

def main():
    print("Loading feature data and trained model...")
    df, model = load_data_and_model()

    print("Preparing test split...")
    test_df = split_test_data(df)

    print("Generating predictions...")
    y_test, predictions = generate_predictions(test_df, model)

    print("Saving evaluation results...")
    results_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": predictions
    })
    results_df.to_csv(FIGURES_PATH.parent / "evaluation_results.csv", index=False)

    print("Creating prediction vs actual plot...")
    plot_prediction_vs_actual(y_test, predictions)

    print("Creating residual distribution plot...")
    plot_residuals_distribution(y_test, predictions)

    print("Creating absolute error over time plot...")
    plot_error_over_time(y_test, predictions)

    print(f"Done! Figures saved to {FIGURES_PATH}")

if __name__ == "__main__":
    main()
