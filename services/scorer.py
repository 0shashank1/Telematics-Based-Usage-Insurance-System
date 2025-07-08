def risk_score(prediction):
    return {"low": 0.1, "medium": 0.5, "high": 1.0}.get(prediction, 0.5)

def adjust_premium(base_premium, risk_factor):
    return base_premium * (1 + risk_factor)
