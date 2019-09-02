import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


raw_data = pd.read_csv("factor_5.csv", index_col="date")
raw_data.index = raw_data.index.astype("str")
factor_data = raw_data.loc[:, ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]]

correl_matrix = pd.DataFrame(np.corrcoef(factor_data.T), index=factor_data.T.index, columns=factor_data.T.index)
correl_matrix.to_csv("correl_matrix.csv")

# factor_data.plot()
# plt.xlabel("date")
# plt.ylabel("cumulative value")
# plt.savefig("1_a_1.png")
# plt.show()

for c in factor_data.columns:
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    factor_data[c].plot()
    plt.xlabel("date")
    plt.ylabel("value")
    plt.title("time series plot for {}".format(c))
    plt.subplot(122)
    plt.hist(factor_data[c], bins=20, label="hist",
             alpha=0.4, density=True)
    sns.kdeplot(factor_data[c], label="fit")
    plt.xlabel("value")
    plt.ylabel("density")
    plt.title("density plot for {}".format(c))
    plt.savefig("1_a_{}.png".format(c))
    plt.show()






