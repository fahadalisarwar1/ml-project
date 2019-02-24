import pandas as pd

print("*******************************loading data from Files*******************************")

data_error = pd.read_csv('/home/fahad/project/ml-project/data/raw/errors.csv')
error_date = data_error.iloc[:, 0].values
error_mach_id = data_error.iloc[:, 1].values
error_type = data_error.iloc[:, 2].values


def main():
    if __name__ == "__main__":
        main()
