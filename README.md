# Telematics-Based Usage Insurance System

This project is a complete AI/ML-powered insurance system that uses **telematics data** to assess driving behavior, assign risk levels (`low`, `medium`, `high`), and provide **usage-based insurance pricing** with safety feedback.

---

## Features

-  **Behavior Analysis:** Detects risky driving using telematics (speed, RPM, throttle, acceleration)
-  **Machine Learning:** Trained `RandomForestClassifier` to classify risk levels
-  **Premium Adjustment:** Dynamically adjusts insurance premiums based on real behavior
-  **Streamlit Frontend:** Clean, responsive UI to input driving stats and get feedback
-  **Model Persistence:** Trained model is saved and reused for predictions

---

## 🗂 Project Structure

```
Telematics-Based-Usage-Insurance/
├── backend/
│   ├── app.py                # Streamlit app
│   ├── services/
│   │   └── analyzer.py       # Model loading and behavior analysis
│   ├── model/
│   │   └── behavior_model.pkl # Saved ML model
│   ├── Telematicsdata.csv    # Raw data used for training
│   └── train_model.py        # Data preprocessing and model training
├── requirements.txt
├── README.md
```

---

##  How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/0shashank1/Telematics-Based-Usage-Insurance-System.git
cd Telematics-Based-Usage-Insurance-System/backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model (Optional)

```bash
python train_model.py
```

### 4. Run the Streamlit App

```bash
python -m streamlit run app.py
```

---

##  Sample Input to Test

| Field              | Value   |
|--------------------|---------|
| Vehicle Speed      | `80`    |
| Engine RPM         | `3000`  |
| Throttle Position  | `40`    |
| Acceleration X     | `0.8`   |
| Acceleration Y     | `0.4`   |
| Acceleration Z     | `0.3`   |

Expected Output:
```
Risk Level: low
Risk Score: 0.10
Adjusted Premium: ₹5500
```

---

##  Model Performance

- Achieved **100% accuracy** on the test set (with `low`, `medium` classes)
- Uses `RandomForestClassifier` with 4 key features
- Preprocessing includes feature extraction (`accel_mag`) and risk label generation

---

##  Requirements

- Python 3.9+
- pandas, numpy, scikit-learn
- streamlit
- matplotlib (optional for plots)

Install via:

```bash
pip install -r requirements.txt
```

---

##  Privacy Consideration

- All analysis is done on anonymized feature-level data.
- Real-world implementation should consider data encryption, consent, and transparency.

---

##  Future Improvements

- Add real-time telematics streaming integration
- Support for more sensors (e.g., braking, GPS)
- Deploy on HuggingFace Spaces or Streamlit Cloud
- Improve UI with charts and driver safety recommendations

---
