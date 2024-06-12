from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_capital_invested(input_file, output_file):
    data = pd.read_csv(input_file)
    model = ARIMA(data['Capital Invested (M USD)'], order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)  # Forecasting the next year, month-wise
    forecast.to_csv(output_file, header=True)

if __name__ == "__main__":
    forecast_capital_invested('data/processed/processed_data.csv', 'data/processed/forecast_results.csv')
