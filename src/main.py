from get_data.first_dataset import get_data as first_dataset
from get_data.second_dataset import get_data as second_dataset
from Dataset import Dataset


def main(dataset: Dataset):
    if dataset == Dataset.FIRST:
        data = first_dataset()
    elif dataset == Dataset.SECOND:
        data = second_dataset()
    else:
        data = []


if __name__ == '__main__':
    main(Dataset.SECOND)
