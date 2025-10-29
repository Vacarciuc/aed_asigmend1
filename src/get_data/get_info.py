import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame

def get_info(
    df: DataFrame,
    column_name: str
):
    if column_name not in df.columns:
        print(f"❌ Coloana '{column_name}' nu există în DataFrame!")
        print(f"Coloane disponibile: {list(df.columns)}")
        return

    # dacă Time nu e numeric, o convertim la datetime
    if not np.issubdtype(df['Time'].dtype, np.number):
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

    data_array = df[column_name]

    print('📊 Date relevante pentru coloana:', column_name)
    print(f'Min: {data_array.min()}')
    print(f'Max: {data_array.max()}')
    print(f'Mean: {data_array.mean()}')
    print(f'Median: {data_array.median()}')
    print(f'Percentila 80%: {np.percentile(data_array.dropna(), 80)}')

    # grafic
    sns.scatterplot(data=df, x='Time', y=column_name)
    title = f'Distribuția valorilor pentru {column_name}'

    plt.title(title)
    plt.xlabel('Timp')
    plt.ylabel(column_name)
    plt.show()
