import pandas as pd

def extract_features(data):
    df = pd.DataFrame([data])
    df['accel_mag'] = (df['ACCELERATION X']**2 + df['ACCELERATION Y']**2 + df['ACCELERATION Z']**2) ** 0.5
    return df[['Vehicle speed', 'ENGINE RPM', 'THROTTLE POSITION', 'accel_mag']].iloc[0]
