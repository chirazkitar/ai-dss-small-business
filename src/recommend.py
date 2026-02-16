def classify_performance(predicted_revenue: float) -> str:

    if predicted_revenue >= 8000:
        return "High Growth Business"
    elif predicted_revenue >= 4000:
        return "Stable Business"
    return "Low Performance Business"


def generate_strategy(performance_tier: str) -> str:

    if performance_tier == "High Growth Business":
        return "Increase marketing investment and consider expansion."
    if performance_tier == "Stable Business":
        return "Optimize conversion rate and improve customer retention."
    return "Reduce operational costs and redesign marketing strategy."