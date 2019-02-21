import pandas as pd

print("*******************************loading data from Files*******************************")

data = pd.read_csv('G:/projects/ml-project/data/raw/machines.csv')
mach_ID = data.iloc[:, 0].values
mach_model = data.iloc[:, 1].values
mach_age = data.iloc[:, 2].values


def main():
    if __name__ == "__main__":
        main()
