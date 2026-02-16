def generate_summary(predicted_revenue: float,
                     performance_tier: str,
                     strategy: str) -> str:
    return (
        f"Predicted monthly revenue: {predicted_revenue:.2f}. "
        f"Business classified as: {performance_tier}. "
        f"Recommended action: {strategy}"
    )