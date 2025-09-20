import pandas as pd


df=pd.read_csv("data.csv")


# wyswietla pierwsze 10 ... wierszy ... znaczy ile wpiszesz bez parametru wyswietla 5
print(df.head(10))
print("=" * 30)

# wyswietla ostnie 5 wierszy bez parametru
print(df.tail())
print("=" * 30)

print(df.info())

print("=" * 30)