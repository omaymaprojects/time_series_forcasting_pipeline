import pandas as pd

def preprocess_data(input_file, output_file):
    data = pd.read_csv(input_file)
    # Example preprocessing steps:
    data.fillna(method='ffill', inplace=True)  # Fill missing values
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw/private_equity_energy_metrics.csv', 'data/processed/processed_data.csv')
