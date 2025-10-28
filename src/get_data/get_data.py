import os
import pandas as pd


def read_file(path:str) -> pd.DataFrame:
    file_path = os.path.join(os.path.dirname(__file__), path)
    df = pd.read_excel(file_path, sheet_name="data", header=None)
    df.columns = df.iloc[0]
    df = df.drop(0)
    # Setăm coloana 'Indicator' ca index și transpunem
    df = df.set_index('Indicator').T
    # Resetăm index-ul numeric într-o coloană 'time'
    df = df.reset_index().rename(columns={'index': 'time'})
    # Redenumește coloana Indicator în Time
    df = df.rename(columns={0: 'Time'})
    #aplicarea filtrelor de curatare
    #detectarea si stergerea valorilor null/lipsa
    df.isnull().sum()
    df.dropna(inplace=True)
    # Verifică coloanele finale
    print('Columns', df.columns)
    return df
