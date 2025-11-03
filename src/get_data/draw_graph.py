import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas import DataFrame
import itertools

def plot_histogram_seaborn(
        data: DataFrame,
        column_name: str,
):
    if column_name not in data.columns:
        print(f"❌ Coloana '{column_name}' nu există în DataFrame!")
        return

    data_array = data[column_name]
    n = len(data_array)
    bins = int(np.ceil(np.log2(n) + 1))
    color = "skyblue"
    title = column_name

    plt.figure(figsize=(8, 5))
    sns.histplot(data_array.dropna(), bins=bins, color=color, kde=True)

    plt.title(title if title else f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()


def plot_box_plot_seaborn(
        data: DataFrame,
        column_name: str
):
    if column_name not in data.columns:
        print(f"❌ Coloana '{column_name}' nu există în DataFrame!")
        return
    sns.boxplot(x=data[column_name], color="skyblue", orient="h", showmeans=True)
    plt.title("Boxplot pentru " + column_name)
    plt.show()


def plot_density_plot(
        data: DataFrame,
        column_name: str
):
    sns.kdeplot(data=data, x=column_name, fill=True, color="skyblue")
    plt.title(f"Density Plot pentru {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Densitate")
    plt.show()


def scatter_plots_multi(data: pd.DataFrame, cols: list[str] = None):
    # Verificăm coloana Time
    if 'Time' not in data.columns:
        print('Coloana "Time" nu a fost găsită în DataFrame!')
        return

    # Convertim Time în datetime
    try:
        data['Time'] = pd.to_datetime(data['Time'])
    except Exception:
        print('Eroare la conversia coloanei Time în datetime.')
        return

    x_axis = data['Time']
    colors = ['green', 'red', 'blue', 'yellow', 'orange', 'gray', 'purple', 'maroon', 'violet', 'coral']

    plt.figure(figsize=(10, 6))

    # Selectăm doar coloanele dorite
    if cols:
        columns_to_plot = [col for col in cols if col in data.columns]
        if not columns_to_plot:
            print("Niciuna dintre coloanele specificate nu există în DataFrame.")
            return
    else:
        columns_to_plot = [c for c in data.columns if c not in ['Indicator', 'Time']]

    # Desenăm punctele
    for i, col in enumerate(columns_to_plot):
        plt.scatter(x_axis, data[col], label=col, color=colors[i % len(colors)], alpha=0.7)

    plt.title('Multi Scatter Plot (Date pe axa timpului)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()