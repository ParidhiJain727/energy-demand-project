import json
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

from app.core.config import FEATURE_COLUMNS

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models/trained_model.pkl"
METRICS_PATH = BASE_DIR / "reports/metrics.json"
REPORTS_PATH = BASE_DIR / "reports"

@st.cache_data
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_metrics():
    if not METRICS_PATH.exists():
        return None
    with open(METRICS_PATH, "r") as f:
        return json.load(f)

def build_input_dataframe(
        hour: int,
        day_of_week: int,
        month: int,
        is_weekend: bool,
        lag_1: float,
        lag_24: float,
        rolling_mean_24: float,
        rolling_std_24: float,
) -> pd.DataFrame:
    data = {
        "hour": hour,
        "day_of_week": day_of_week,
        "month": month,
        "is_weekend": is_weekend,
        "lag_1": lag_1,
        "lag_24": lag_24,
        "rolling_mean_24": rolling_mean_24,
        "rolling_std_24": rolling_std_24,
    }

    df = pd.DataFrame([data])
    return df[FEATURE_COLUMNS]
