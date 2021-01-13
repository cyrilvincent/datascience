# Charger avec pandas data_with_nan
# Il y a 2 stratégies
#   fillna(0) => calculer mean et std
#   dropper les 3 colonnes slope,ca,thal + dropna => mean et std
# Sauvegarder le minage avec to_csv (dataclean.csv)
# Etudier les 4 colonnes age, sex, trestbps, chol pour num = 1 et 0

import pandas as pd
import numpy as np

def mean_std(serie):
    return np.mean(serie), np.std(serie)

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop("slope", axis=1).drop("ca", 1).drop("thal", 1)
print(dataframe.shape)
datamart = dataframe.dropna()
print(datamart.shape)
print(mean_std(datamart[datamart.num == 0].age))
print(mean_std(datamart[datamart.num == 1].age))
print(mean_std(datamart[datamart.num == 0].sex))
print(mean_std(datamart[datamart.num == 1].sex))
print(mean_std(datamart[datamart.num == 0].trestbps))
print(mean_std(datamart[datamart.num == 1].trestbps))
print(mean_std(datamart[datamart.num == 0].chol))
print(mean_std(datamart[datamart.num == 1].chol))
datamart.to_csv("data/heartdisease/dataclean.csv")
for row in datamart.iterrows():
    print(row[1].age)
