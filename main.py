import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('data/CH_5_9665_2013_timeseries.csv')
    df = df[['Concentration', 'DatetimeBegin']]
    df = df.sort_values(by='DatetimeBegin')
    print(df)