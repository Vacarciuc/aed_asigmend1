from get_data.get_data import read_file
from get_data.get_info import get_info
from get_data.draw_graph import plot_histogram_seaborn
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

    data = read_file(path)
    plot_histogram_seaborn(data, "earn_nt_net")
    # get_info(
    #     column_name='earn_nt_net',
    #     df=data,
    #     start_year=2001,
    #     end_year=2022,
    # )


if __name__ == '__main__':
    main(Dataset.THIRD)



