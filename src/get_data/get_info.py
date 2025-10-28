import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame

def get_info(column_name: str, df: DataFrame, start_year: int = None, end_year: int = None):
    if column_name not in df.columns:
        print(f"❌ Coloana '{column_name}' nu există în DataFrame!")
        print(f"Coloane disponibile: {list(df.columns)}")
        return

    # dacă Time nu e numeric, o convertim la datetime
    if not np.issubdtype(df['Time'].dtype, np.number):
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

    # aplicăm filtrarea după ani dacă se specifică
    if start_year and end_year:
        mask = (df['Time'].dt.year >= start_year) & (df['Time'].dt.year <= end_year)
        df = df.loc[mask]
        print(f"📅 Filtrat pentru perioada {start_year} - {end_year} ({len(df)} rânduri)")

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
    if start_year and end_year:
        title += f' ({start_year}-{end_year})'
    plt.title(title)
    plt.xlabel('Timp')
    plt.ylabel(column_name)
    plt.show()
