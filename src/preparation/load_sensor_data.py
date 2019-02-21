import pandas as pd

print("*******************************loading data from Files*******************************")

data = pd.read_csv('G:/projects/ml-project/data/raw/telemetry.csv')
sens_date = data.iloc[:, 0].values
sens_id = data.iloc[:, 1].values
sens_volt = data.iloc[:, 2].values
sens_rot = data.iloc[:, 3].values
sens_pres = data.iloc[:, 4].values
sens_vib = data.iloc[:, 5].values


def main():
    if __name__ == "__main__":
        main()
