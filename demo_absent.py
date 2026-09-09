import pandas as pd

df = pd.read_csv("data/absenteeism_at_work/Absenteeism_at_work.csv", delimiter=";", index_col="ID")
print(df.isna().sum())
print(df.groupby('Absenteeism time in hours').size())

bins = [-1, 0, 4, 8, 24, df["Absenteeism time in hours"].max()]
labels = ['Aucune', 'Courte (1-4h)', 'Demi-journée (5-8h)', 'Longue (9-24h)', 'Très longue (>24h)']

df["categories"] = pd.cut(df["Absenteeism time in hours"], bins=bins, labels=False)
print(df["categories"])

