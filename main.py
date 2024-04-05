import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(data, period):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='DatetimeBegin', y='Concentration', data=data)
    plt.title(f"PM10 {period}")
    plt.xlabel("Date")
    plt.ylabel("PM10")
    plt.tight_layout()
    plt.savefig(f'charts/concentration-{period}.png', dpi=500)
    plt.close()


if __name__ == '__main__':
    df = pd.read_csv('data/CH_5_9665_2013_timeseries.csv')
    df = df[['Concentration', 'DatetimeBegin']]
    df['DatetimeBegin'] = pd.to_datetime(df['DatetimeBegin'])
    df = df.sort_values(by='DatetimeBegin')
    df['Month'] = df['DatetimeBegin'].dt.month_name()

    print('Start generating charts...')
    sns.set_style('whitegrid')
    #Annually
    plot_data(df, 'Annually')
    # Monthly
    for month in df['Month'].unique():
        plot_data(df[df['Month'] == month], month)
    print('Finish generating charts...')