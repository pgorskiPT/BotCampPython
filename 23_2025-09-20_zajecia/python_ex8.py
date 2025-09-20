import pandas as pd
from jupyter_core.migrate import regex

data = pd.read_csv('data_with_date.csv')
print(data)
print(data.loc[[7, 10]])
print("=" * 30)

data.loc[7, "Duration"] = 45
print(data.loc[7])

print(data.loc[[7, 10]])
print("=" * 30)

data = pd.read_csv('data_with_date.csv')

for x in data.index:
    if data.loc[x, 'Duration'] > 120:
        data.loc[x, 'Duration'] = 120
print(data)
print("=" * 30)

data = pd.read_csv('data_with_date.csv')
for x in data.index:
    if data.loc[x, "Duration"] > 120:
        data.drop(x, inplace=True)
print(data)

print("=" * 30)

# te same zadania w sposob pandasowy
# jesli wartosci beda powyzej 120 zostana zrownane/zmienione na 120
data = pd.read_csv('data_with_date.csv')
data['Duration'] = data['Duration'].clip(upper=120)
print(data)
print("=" * 30)

# where, wyszukacj spelniajace warunek, zmien na 120
data = pd.read_csv('data_with_date.csv')
data['Duration'] = data['Duration'].where(data['Duration'] <= 120, 120)
print(data)
print("=" * 30)

# odwrotnosc where , zamaskuj spelniajace warunek ustaw wartosc
data = pd.read_csv('data_with_date.csv')
data['Duration'] = data['Duration'].mask(data['Duration'] > 120, 120)
print(data)
print("=" * 30)

# filtrowanie
data = pd.read_csv('data_with_date.csv')
data = data[data['Duration'] <= 120]
print(data)
print("=" * 30)
print("=" * 30)

data = pd.read_csv('data_with_date.csv')
data = data.query("Duration<=120")
print(data)
print("=" * 30)

# różnice w wszybkosci metod Python kontra pandas a wlasciwie numpy w tle pandasa
# Method               Rows in    Time [s]   Rows remaining
# for + drop(per-row)  10000      0.973      6103
# boolean filter       1000000    0.0119     602352
# mask + drop(once)    1000000    0.0271     601573
print("=" * 30)
df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
print(df)

# # starsza metoda zamieni i zwroci informacje o przyszlym beledzie
# df['Miasto'].replace("Warszawa","Warszawa-Stolica", inplace=True)
# print(df)   # wypisze pierwsze 60 wierszy
# print(df.to_string()) # wypisyje wiecej niz 60 wierszy
print("=" * 30)

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace("Warszawa", "Warszawa-Stolica")
# print(df)   # wypisze pierwsze 60 wierszy
print(df.to_string())  # wypisyje wiecej niz 60 wierszy
#              Miasto
# 0  Warszawa-Stolica
# 1            Kraków
# 2              Łódź
# 3  Warszawa-Stolica
# 4           Gliwice
print("=" * 30)

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace({"Warszawa": "Warszawa-Stolica", "Kraków": "Krakow - Zamkowy"})
# print(df)   # wypisze pierwsze 60 wierszy
print(df.to_string())  # wypisyje wiecej niz 60 wierszy
#              Miasto
# 0  Warszawa-Stolica
# 1  Krakow - Zamkowy
# 2              Łódź
# 3  Warszawa-Stolica
# 4           Gliwice
print("=" * 30)

import time

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40]})
print(df)
print("=" * 30)
df["Kategoria"] = "Dorosły"
print(df)
start_time = time.time()  # start pomiaru czasu
df.loc[df['Wiek'] < 18, "Kategoria"] = "Niepełnolietni"
end_time = time.time()  # koniec pomiaru czasu
print("=" * 30)
print(df)
print("=" * 30)
print(f"Czas wykonania: {end_time - start_time:.6f} sekundy")

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace(r"^Ł.*", "Łódź Przemysłowa", regex=True)
# df['Miasto']=df['Miasto'].replace("Łódź","Łódź Przemysłowa", regex=True)
print(df.to_string())

# prametr regex
# Podsumowanie
# ^ oznacza początek tekstu,
# .* to dowolne znaki po znaku Ł,
# Ten regex dopasuje cały łańcuch zaczynający się od "Ł",
# Właśnie dlatego pandas zastępuje cały tekst, a nie tylko sam znak Ł.
# Tak działają wyrażenia regularne w pandas replace z opcją regex=True.
# To pozwala precyzyjnie kontrolować, które fragmenty tekstu są zamieniane.

print("=" * 30)
df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40, 65]})

df['Kategoria'] = df['Wiek'].apply(lambda x: "Senior" if x > 60 else "Dorosły")
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły
# 5    65    Senior
print("=" * 30)


def zmienna(x):
    if x > 60:
        return "Senior"
    else:
        return "Dorosły"


df['Kategoria'] = df['Wiek'].apply(zmienna)
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły
# 5    65    Senior
print("=" * 30)

df = pd.DataFrame({'Miasto': ['Warszawa123', 'Kraków456', "Łódź", "Warszawa789", "Gli789wice"]})
print(df)
#         Miasto
# 0  Warszawa123
# 1    Kraków456
# 2         Łódź
# 3  Warszawa789
# 4   Gli789wice
print("=" * 30)
df['Miasto'] = df['Miasto'].replace(r"\d+", "", regex=True)
print(df)
#      Miasto
# 0  Warszawa
# 1    Kraków
# 2      Łódź
# 3  Warszawa
# 4   Gliwice
print("=" * 30)


