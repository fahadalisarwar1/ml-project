import pandas as pd

print("*******************************loading data from Files*******************************")

data_sens = pd.read_csv('G:/projects/ml-project/data/raw/telemetry.csv')
sens_date = data_sens.iloc[:, 0].values
sens_id = data_sens.iloc[:, 1].values
sens_volt = data_sens.iloc[:, 2].values
sens_rot = data_sens.iloc[:, 3].values
sens_pres = data_sens.iloc[:, 4].values
sens_vib = data_sens.iloc[:, 5].values


def main():
    if __name__ == "__main__":
        main()
