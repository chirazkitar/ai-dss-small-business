# Explainable AI Decision Support System for Small Businesses


## 1.Project Overview
Small businesses often collect sales and marketing data but struggle to extract clear insights or actionable decisions from it.


This project aims to build an **Explainable AI Decision Support System (DSS)** that helps small businesses:
- Predict future sales performance
- Understand the key factors driving these predictions
- Receive actionable, data-driven recommendations


The focus is not only on prediction accuracy, but also on **transparency, interpretability, and real-world usability**.



## Objectives
- Build a machine learning model to predict monthly revenue
- Apply Explainable AI techniques to interpret model predictions
- Generate clear business recommendations based on data insights
- Deliver results through an interactive dashboard



## Dataset
Due to data privacy constraints commonly faced by small businesses, this project uses a **realistically generated synthetic dataset** that simulates monthly sales and marketing operations.


The dataset captures:
- Marketing spend and website traffic
- Customer conversion behavior
- Discounts and seasonality effects
- Monthly revenue as the target variable


Synthetic data allows full control over feature design while preserving realistic business dynamics.


## AI Tasks
- **Prediction:** Monthly revenue forecasting (regression)
- **Explainability:** Feature importance and SHAP-based explanations
- **Decision Support:** Rule-based and AI-informed recommendations


## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost / Random Forest
- SHAP (Explainable AI)
- Streamlit (Dashboard)



## Project Structure
ai-dss-small-business/
├── data/
│   ├── raw/
│   │   └── small_business_sales.csv
    └──`generate_synthetic_data.py` → Synthetic data generator
├── notebooks/
│   └── `01_synthetic_data_explained.ipynb` → Step-by-step explanation
├── src/
├── app/
├── README.md


## Project Status
**In progress** — development is organized into clear phases:
1. Dataset generation & analysis
2. Model training & evaluation
3. Explainable AI integration
4. Decision recommendation engine
5. Dashboard & final polish