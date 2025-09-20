import pandas as pd

df = pd.read_csv('data.csv')
# print(df.to_string())

print(df.head())
print("=" * 30)


print(df.corr())
print("=" * 30)

import seaborn as sns
import matplotlib.pyplot as plt

#korelacje = df.corr()
# print(korelacje)
# Rysowanie heatmapy
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True, linewidths=0.5)
plt.show()