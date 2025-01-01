import pandas as pd

data = pd.read_csv("train.csv")
df = data[data[["Text", "Sentiment"]].notnull().all(1)]

df.to_csv("out.csv", header=True, index=False)

