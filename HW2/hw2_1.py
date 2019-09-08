import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


df = pd.read_csv("hw2_1.csv", index_col="date", parse_dates=["date"])

df["RET-RF"] = df["RET"] - df["RF"]

X = df.loc[:, ["Mkt-RF", "HML", "SMB", "RMW", "CMA"]]
y = df["RET-RF"]

X = sm.add_constant(X)
model = sm.OLS(y, X)

res = model.fit()
print(res.summary())



