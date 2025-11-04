from pandas import DataFrame

from get_data.get_data import read_file
from get_data.get_info import get_info
from get_data.draw_graph import plot_histogram_seaborn
from get_data.draw_graph import plot_box_plot_seaborn
from get_data.draw_graph import plot_density_plot
from get_data.draw_graph import scatter_plots_multi
from get_data.get_data import get_zero_code
from get_data.get_info import get_heat_map
from get_data.get_data import add_growth_rate
from get_data.get_data import filer_data_hp_bidirectional
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
    #hp-filter datele mele devin ma dispersate...
    #data = filer_data_hp_bidirectional(data)
    data = add_growth_rate(data, 'namq_10_exi')
    data = add_growth_rate(data, 'namq_10_gdp')
    univariate_analysis(
        data=data,
        column_name='namq_10_gdp',
    )
    z_score_data = get_zero_code(data)
    bivariate_analysis(z_score_data)



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
    coo_array = ['namq_10_gdp', 'une_rt_q', 'demo_pjan']
    scatter_plots_multi(data, coo_array)
    get_heat_map(data)


if __name__ == '__main__':
    main(Dataset.FIRST)


