import time
import pandas as pd
import polars as pl
import  dask.dataframe as dd

filename = "bigfile_polars.csv"

# polras (read)

start = time.time()
df_polars = pl.read_csv(filename)
filtered_polars = df_polars.filter(pl.col('category') == 'B')
print("Polars read: liczba wierszy z kategorii 'B':", filtered_polars.height)
print("Polars read filter czas:", time.time() - start)


# Polars (scan, czyli lazy - nie tryma całego pliku w RAM

start = time.time()
df_polars = pl.scan_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B").collect()
print("Polars scan: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars scan filter czas:", time.time() - start)


# pandas

start = time.time()
df_pandas = pd.read_csv(filename)
filtered_pandas = df_pandas[df_pandas["category"] == "B"]
print("Pandas read: liczba wierszy z kategorią 'B':", len(filtered_pandas))
print("Pandas read filter czas:", time.time() - start)


#dask
df=dd.read_csv(filename)
filter_dask=df[df['category']=="B"]

start = time.time()
result = filter_dask.shape[0].compute()
end=time.time()
print("Dask read: liczba wierszy z kategorią 'B':", result)
print("Dask read filter czas:", end - start)