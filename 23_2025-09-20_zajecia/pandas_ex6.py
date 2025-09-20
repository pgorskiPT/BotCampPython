from unittest.mock import inplace

import pandas as pd

df = pd.read_csv("data.csv")

rows_with_nan = df[df.isnull().any(axis=1)]
print(rows_with_nan)
print("=" * 30)

df.fillna(130, inplace=True)
print(df.info())
print("=" * 30)
print(df.loc[[10, 17, 27, 91, 118, 141, 168]])
print("=" * 30)

df = pd.read_csv("data.csv")

rows_with_nan = df[df.isnull().any(axis=1)]
print(rows_with_nan)
print("=" * 30)

df.fillna({"Calories": 130}, inplace=True)
df.info()
print("=" * 30)
print(df.loc[[10, 17, 27, 91, 118, 141, 168]])
print("=" * 30)

df = pd.read_csv("data.csv")

rows_with_nan = df[df.isnull().any(axis=1)]
print(rows_with_nan)
print("=" * 30)
df['Calories'] = df['Calories'].fillna(130)
df.info()
print("=" * 30)
print(df.loc[[10, 17, 27, 91, 118, 141, 168]])

# print("=" * 30)
# # df = pd.read_csv("data.csv")
# df['Calories'].fillna(130, inplace=True)
# df.info()
# print("=" * 30)

print("=" * 30)
# srednia arytmetyczna
df = pd.read_csv("data.csv")

x=df['Calories'].mean()
print("Srednia wynosi:", x)


print("=" * 30)
df['Calories'] = df['Calories'].fillna(x)

print(df.loc[[10, 17, 27, 91, 118, 141, 168]])
print("=" * 30)

#mediana
# Przykładowy DataFrame
df = pd.DataFrame({
    'A': [2, 4, 6, 8, 10],
    'B': [1, 3, 5, 7, 9],
    'C': [4, 6, 1, 9, 3]
})

# Obliczenie mediany dla każdej kolumny
medians = df.median()
print(medians)

print("=" * 30)
data={"wiek":[25,30,35,40,45,50,55,60,65]}
df=pd.DataFrame(data)
mediana_wieku=df['wiek'].median()
print("Mediana wieku:", mediana_wieku)
print("=" * 30)


df = pd.read_csv("data.csv")
mediana_calorie=df['Calories'].median()
print("Mediana calorie:", mediana_calorie)
print("=" * 30)

df['Calories'] = df['Calories'].fillna(mediana_calorie)

print(df.loc[[10, 17, 27, 91, 118, 141, 168]])
print("=" * 30)
print(df.loc[141])
print("=" * 30)

#mode() - moda - wartosc najczesciej wystepujaca

df = pd.read_csv("data.csv")
mode_data=df["Calories"].mode()
print(" Najczesciej wystepujace:",mode_data)
print("=" * 30)
print(type(mode_data))
print("=" * 30)
print(mode_data)
print("=" * 30)
df["Calories"]=df['Calories'].fillna(mode_data[0])
print(df.loc[[10, 17, 27, 91, 118, 141, 168]])
print("=" * 30)

df = pd.read_csv("data.csv")
rows_with_nan = df[df.isna().any(axis=1)]
print(rows_with_nan)
print("=" * 30,"nastepny")
print(df[df["Calories"].isna()])