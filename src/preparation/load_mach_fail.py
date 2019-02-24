import pandas as pd

print("*******************************loading data from Files*******************************")

data_fail = pd.read_csv('/home/fahad/project/ml-project/data/raw/failures.csv')
fail_date = data_fail.iloc[:, 0].values
fail_mach_id = data_fail.iloc[:, 1].values



def main():
    if __name__ == "__main__":
        main()
