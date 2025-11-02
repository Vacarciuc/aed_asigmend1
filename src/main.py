from pandas import DataFrame

from get_data.get_data import read_file
from get_data.get_info import get_info
from get_data.draw_graph import plot_histogram_seaborn
from get_data.draw_graph import plot_box_plot_seaborn
from get_data.draw_graph import plot_density_plot
from get_data.draw_graph import scatter_plots_multi
from get_data.get_data import get_zero_code
from get_data.get_info import get_heat_map
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
    univariate_analysis(
        data=data,
        column_name='earn_nt_net',
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
    scatter_plots_multi(data)
    get_heat_map(data)


if __name__ == '__main__':
    main(Dataset.THIRD)


#dataset_1
#relatie puternica pozitiva
# [('lfsi_emp_q', 'tipsna40', 'namq_10_exi', 'namq_10_gdp'),
#relatie puternica negativa
#[('lfsi_emp_q', 'une_rt_q')]fil

#dataset_2
#relatie puternica pozitiva
#[('prc_hicp_manr', 'FP.CPI.TOTL.ZG'),
# ('ert_bil_eur_m','prc_hicp_midx\n', 'mabmm301huq189s', 'namq_10_gdp'),

#dataset_3
#relatie puternica pozitiva
#[('prc_hicp_manr', 'FP.CPI.TOTL.ZG'),
# ('earn_nt_net', 'namq_10_gdp', 'nama_10_lp_ulc'),

