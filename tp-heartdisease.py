# Charger avec pandas data_with_nan
# Il y a 2 stratégies
#   fillna(0) => calculer mean et std
#   dropper les 3 colonnes slope,ca,thal + dropna => mean et std
# Sauvegarder le minage avec to_csv (dataclean.csv)
# Etudier les 4 colonnes age, sex, trestbps, chol pour num = 1 et 0

import pandas as pd
dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop("slope", axis=1).drop("ca", 1).drop("thal", 1)

