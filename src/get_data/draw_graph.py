import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_histogram_seaborn(
        data,
        column_name,
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