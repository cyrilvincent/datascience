import pandas as pd
print(pd.__version__)

dataframe = pd.read_csv("data/house/house.csv",na_values=".")
pd.read_excel("data/house/house.xslx",0)
print(dataframe.loyer / dataframe.surface)
dataframe = dataframe[dataframe.surface < 200]

