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


def scatter_plots_multi(data: DataFrame):
    colors = 'green', 'red', 'blue', 'yellow', 'orange', 'gray', 'purple', 'maroon', 'violet', 'coral'
    if 'Time' not in data.columns:
        return
    x_axis = data['Time']
    for col in data.columns[1:]:
        plt.scatter(x_axis, data[col], label=col)

    plt.title('Multi Scatter Plot (DataFrame cu coloane multiple)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()