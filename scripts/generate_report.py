import pandas as pd
import matplotlib.pyplot as plt

def generate_report(data_file, report_file):
    data = pd.read_csv(data_file)
    plt.figure(figsize=(10, 5))
    plt.plot(data['forecast'])
    plt.title('Forecast of Capital Invested')
    plt.savefig(report_file)

if __name__ == "__main__":
    generate_report('data/processed/forecast_results.csv', 'report.pdf')

