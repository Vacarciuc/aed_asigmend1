import os.path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def get_data():
    file_path = os.path.join(os.path.dirname(__file__), "../../data/dataset_1.xlsx")
    df = pd.read_excel(file_path, sheet_name="data", header=None)
    df.columns = df.iloc[0]
    df = df.drop(0)
    # Setăm coloana 'Indicator' ca index și transpunem
    df = df.set_index('Indicator').T
    # Resetăm index-ul numeric într-o coloană 'time'
    df = df.reset_index().rename(columns={'index': 'time'})
    # Redenumește coloana Indicator în Time
    df = df.rename(columns={0: 'Time'})
    # Verifică coloanele finale
    print('Columns', df.columns)
    # Setează date în variabile pentru a manipula mai ușor cu ele
    time_array = df['Time']
    data_array = df['tipsna40']

    print('Date relevante')
    print('Min', data_array.min())
    print('Macx', data_array.max())
    print('Mean', data_array.mean())
    print('Median', data_array.median())
    print('Percentila 80%:', np.percentile(data_array.dropna(), 80))

    sns.scatterplot(data=df, x=time_array, y=data_array)
    plt.title('Scatter tipsna40')
    plt.show()
    return df