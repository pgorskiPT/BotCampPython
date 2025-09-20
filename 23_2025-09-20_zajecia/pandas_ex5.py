import pandas as pd


df=pd.read_csv("data.csv")



new_df=df.dropna()
print(new_df.to_string())
print("=" * 30)


print(new_df.info())

print("=" * 30)

rows_with_nan = df[df.isnull().any(axis=1)]
print(rows_with_nan)
print("=" * 30)


df.dropna(inplace=True)
print(df.info())