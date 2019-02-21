import pandas as pd

print("*******************************loading data from Files*******************************")

data_mach = pd.read_csv('G:/projects/ml-project/data/raw/machines.csv')
mach_ID = data_mach.iloc[:, 0].values
mach_model = data_mach.iloc[:, 1].values
mach_age = data_mach.iloc[:, 2].values


def main():
    if __name__ == "__main__":
        main()
