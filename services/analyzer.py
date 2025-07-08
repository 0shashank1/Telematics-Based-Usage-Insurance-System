import pandas as pd
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "../model/behavior_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def analyze_behavior(features):
    # Ensure DataFrame with correct columns
    df = pd.DataFrame([features])
    return model.predict(df)[0]
