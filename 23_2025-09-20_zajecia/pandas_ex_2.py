import pandas as pd

df = pd.read_csv("data.csv")
print(df)
print("=" * 30)


#wyswuektabie wszystkich wierszy
print(df.to_string())


print("=" * 30)

#pokazuje paramet po jakim ilosci danych dane zostaja wczytane jako czastkwoe #60
print(pd.options.display.max_rows)
# 60

print("=" * 30)

pd.options.display.max_rows=9999
print(df)
print(pd.options.display.max_rows)


print("=" * 30)
pd.options.display.max_rows=60
print(pd.options.display.max_rows)

print("=" * 30)

