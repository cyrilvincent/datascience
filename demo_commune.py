# Joindre dans un DF
# Dept & Communes
# Communes & Iris
# Puis CP et communes
# Saisir un CP ca vous affiche les communes liées + Iris + dept
# low_memory=False
# commune_df["dept_id"] = commune_df["dept_id"].astype(str)
# rsuffix='_right'
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
dept_df = pd.read_csv("data/communes/dept.csv", index_col="id")
print(dept_df.head(10))

communes_df = pd.read_csv("data/communes/communes.csv", low_memory=False, index_col="id")
print(communes_df.head(10))
dept_df["dept_id"] = dept_df.index

communes_dept_df = communes_df.join(dept_df, on="dept_id", rsuffix="_dept")
print(communes_dept_df.head(10))

iris_df = pd.read_csv("data/communes/iris.csv", low_memory=False, index_col="id")
print(iris_df.head(10))

communes_dept_iris_df = pd.merge(communes_dept_df, iris_df, left_on="id", right_on="commune_id", suffixes=("", "_iris"))
print(communes_dept_iris_df.head(10))

cp_df = pd.read_csv("data/communes/cp.csv", low_memory=False)
print(cp_df.dtypes)
cp_df["code"] = cp_df["code_insee"]
all_df = pd.merge(communes_dept_iris_df, cp_df, on="code", suffixes=("", "_right"))
print(all_df.head(10))
#
cp = 38250
result = all_df[all_df["code_postal"] == cp]
print(result)
result.to_csv("data/communes/result.csv", index=False)
#
#
#
#
