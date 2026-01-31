import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------
np.random.seed(42)

N_MONTHS = 24  # 2 years of data
START_DATE = "2023-01-01"

OUTPUT_PATH = Path("data/raw")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Generate base timeline
# ----------------------------
dates = pd.date_range(start=START_DATE, periods=N_MONTHS, freq="ME")
months = dates.strftime("%Y-%m")

# ----------------------------
# Business features
# ----------------------------

# Seasonality
seasons = []
for d in dates:
    if d.month in [12, 1, 2]:
        seasons.append("Winter")
    elif d.month in [3, 4, 5]:
        seasons.append("Spring")
    elif d.month in [6, 7, 8]:
        seasons.append("Summer")
    else:
        seasons.append("Autumn")

season_multiplier = {
    "Winter": 0.9,
    "Spring": 1.05,
    "Summer": 1.2,
    "Autumn": 1.0
}

# Marketing spend (in $)
marketing_spend = np.random.randint(2000, 12000, size=N_MONTHS)

# Website visits depend on marketing spend
website_visits = (marketing_spend * np.random.uniform(2.5, 4.0, N_MONTHS)).astype(int)

# Conversion rate (affected by season)
base_conversion = np.random.uniform(0.02, 0.06, N_MONTHS)
conversion_rate = [
    base_conversion[i] * season_multiplier[seasons[i]]
    for i in range(N_MONTHS)
]

# Number of customers
num_customers = (website_visits * conversion_rate).astype(int)

# Average order value (AOV)
avg_order_value = np.random.normal(loc=60, scale=10, size=N_MONTHS)
avg_order_value = np.clip(avg_order_value, 35, 100)

# Discounts (%)
discount_rate = np.random.choice([0, 5, 10, 15, 20], size=N_MONTHS)

# ----------------------------
# Revenue calculation
# ----------------------------
revenue = (
    num_customers
    * avg_order_value
    * (1 - discount_rate / 100)
    * [season_multiplier[s] for s in seasons]
)

# Add realistic noise
revenue = revenue + np.random.normal(0, 2000, size=N_MONTHS)
revenue = revenue.clip(min=0).round(2)

# ----------------------------
# Build DataFrame
# ----------------------------
df = pd.DataFrame({
    "month": months,
    "season": seasons,
    "marketing_spend": marketing_spend,
    "website_visits": website_visits,
    "conversion_rate": np.round(conversion_rate, 4),
    "num_customers": num_customers,
    "avg_order_value": np.round(avg_order_value, 2),
    "discount_rate": discount_rate,
    "revenue": revenue
})

# ----------------------------
# Save dataset
# ----------------------------
output_file = OUTPUT_PATH / "small_business_sales.csv"
df.to_csv(output_file, index=False)

print("Synthetic dataset generated successfully.")
print(f"Saved to: {output_file}")
