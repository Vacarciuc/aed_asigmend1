from pandas import DataFrame

from get_data.get_data import read_file
from get_data.get_info import get_info
from get_data.draw_graph import plot_histogram_seaborn
from get_data.draw_graph import plot_box_plot_seaborn
from get_data.draw_graph import plot_density_plot
from get_data.draw_graph import scatter_plots_multi
from Dataset import Dataset


def main(dataset: Dataset):
    if dataset == Dataset.FIRST:
        path = "../../data/dataset_1.xlsx"
    elif dataset == Dataset.SECOND:
        path = "../../data/dataset_2.xlsx"
    elif dataset == Dataset.THIRD:
        path = "../../data/dataset_3.xlsx"
    else:
        return

    data = read_file(path, started=2000, finished=2024)
    # univariate_analysis(
    #     data=data,
    #     column_name='earn_nt_net',
    # )
    bivariate_analysis(data)


def univariate_analysis(
        data: DataFrame,
        column_name: str,
):
    plot_histogram_seaborn(data, column_name)
    plot_box_plot_seaborn(data, column_name)
    plot_density_plot(data, column_name)
    get_info(data, column_name)


def bivariate_analysis(
    data: DataFrame
):
    scatter_plots_multi(data)


if __name__ == '__main__':
    main(Dataset.THIRD)

