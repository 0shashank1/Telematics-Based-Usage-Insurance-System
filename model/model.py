

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

df_raw = pd.read_csv("Telematicsdata.csv")

selected_vars = [
    'Vehicle speed', 'ENGINE RPM', 'THROTTLE POSITION',
    'ACCELERATION X', 'ACCELERATION Y', 'ACCELERATION Z'
]
df = df_raw[df_raw['variable'].isin(selected_vars)].copy()

df_pivot = df.pivot_table(
    index='timestamp',
    columns='variable',
    values='value',
    aggfunc='first'
).reset_index()

df_pivot[selected_vars] = df_pivot[selected_vars].apply(pd.to_numeric, errors='coerce')
df_pivot.dropna(inplace=True)

df_pivot['accel_mag'] = np.sqrt(
    df_pivot['ACCELERATION X']**2 + 
    df_pivot['ACCELERATION Y']**2 + 
    df_pivot['ACCELERATION Z']**2
)

def assign_risk(row):
    if (row['Vehicle speed'] > 80 and row['accel_mag'] > 10) or \
       (row['ENGINE RPM'] > 3000 and row['THROTTLE POSITION'] > 80):
        return 'high'
    elif row['Vehicle speed'] > 30 or row['THROTTLE POSITION'] > 40:
        return 'medium'
    else:
        return 'low'

df_pivot['risk_label'] = df_pivot.apply(assign_risk, axis=1)

features = ['Vehicle speed', 'ENGINE RPM', 'THROTTLE POSITION', 'accel_mag']
X = df_pivot[features]
y = df_pivot['risk_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

with open("behavior_model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model saved as behavior_model.pkl")
