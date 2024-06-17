from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_capital_invested(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)
    
    # Assuming 'Capital Invested (M USD)' is the primary time series
    # and other columns like 'Number of Deals' and 'ROI (%)' are exogenous variables
    target = data['Capital Invested (M USD)']
    exog = data[['Number of Deals', 'ROI (%)']]  # Include other relevant columns as needed
    
    # Fit the ARIMA model with exogenous variables
    model = ARIMA(target, order=(1, 1, 1), exog=exog)
    model_fit = model.fit()
    
    # Forecasting the next year, month-wise
    # For forecasting, provide future values for the exogenous variables
    # Here, we're assuming the future exog data is a continued pattern or mean of past data
    future_exog = exog.tail(12).mean().to_frame().T.reindex(range(12)).fillna(method='ffill')
    forecast = model_fit.forecast(steps=12, exog=future_exog)
    
    # Print the forecast to verify its content
    forecast_df = pd.DataFrame(forecast, columns=['forecast'])
    print(forecast_df)
    
    # Save the forecast to a CSV file with a column named 'forecast'
    forecast_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    forecast_capital_invested('data/processed/processed_data.csv', 'data/processed/forecast_results.csv')


