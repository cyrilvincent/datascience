import pandas as pd
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp
import sklearn.linear_model as lm
import sklearn.neural_network as nn
import numpy as np

df = pd.read_csv("data/absenteeism_at_work/Absenteeism_at_work.csv", delimiter=";", index_col="ID")
print(df.isna().sum())
print(df.groupby('Absenteeism time in hours').size())

bins = [-1, 0, 4, 8, 24, df["Absenteeism time in hours"].max()]
labels = ['Aucune', 'Courte (1-4h)', 'Demi-journée (5-8h)', 'Longue (9-24h)', 'Très longue (>24h)']

df["categories"] = pd.cut(df["Absenteeism time in hours"], bins=bins, labels=False)
print(df["categories"])

# df['Reason for absence'] = df['Reason for absence'].astype('category')
# df['Month of absence'] = df['Month of absence'].astype('category')
# df['Day of the week'] = df['Day of the week'].astype('category')
# df['Seasons'] = df['Seasons'].astype('category')
# df['Disciplinary failure'] = df['Disciplinary failure'].astype('category')
# df['Education'] = df['Education'].astype('category')
# df['Social drinker'] = df['Social drinker'].astype('category')
# df['Social smoker'] = df['Social smoker'].astype('category')
# df['Pet'] = df['Pet'].astype('category')
df.info()

y = df['categories']
x = df.drop(["categories", "Absenteeism time in hours"], axis=1)
x.reset_index(drop=True)
print(x.columns)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, random_state=42)

model = rf.RandomForestClassifier(random_state=42)
model = nn.MLPClassifier(hidden_layer_sizes=(50,20), activation='relu')
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
ypred = model.predict(xtest)
print(np.mean(np.abs(ytest - ypred)))

# y = df["Absenteeism time in hours"]
# xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, random_state=42)
# model = rf.RandomForestRegressor(random_state=42)
# model = nn.MLPRegressor(hidden_layer_sizes=(50,20), activation='relu')
# model.fit(xtrain, ytrain)
# print(model.score(xtest, ytest))
# ypred = model.predict(xtest)
# print(ytest - ypred)
# print(np.mean(np.abs(ytest - ypred)))

# model = pipe.make_pipeline(
#     pp.StandardScaler(),
#     pp.PolynomialFeatures(degree=5),
#     lm.Ridge()
# )
# model.fit(xtrain, ytrain)
# print(model.score(xtest, ytest))
# ypred= model.predict(xtest)
# print(ytest - ypred)
# print(np.mean(np.abs(ytest - ypred)))