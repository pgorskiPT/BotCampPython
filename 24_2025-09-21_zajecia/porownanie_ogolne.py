import time
import dask.dataframe as dd
import  pandas as pd
import polars as pl


filename = "bigfile_polars.csv"

print(150*"=")
# pandas
start=time.time()

df=pd.read_csv(filename)
mean=df["value"].mean()
print("Pandas mean:", mean)
print("Czas:", time.time()-start)

print(150*"=")
# polars
start=time.time()

df=pl.read_csv(filename)
mean=df["value"].mean()
print("Polars mean:", mean)
print("Czas:", time.time()-start)


print(150*"=")
# polars lazy, scan
start = time.time()
df_lazy = pl.scan_csv(filename)
mean_df = df_lazy.select(pl.col("value").mean()).collect()
mean_lazy = mean_df[0, 0]  # wydobywanie wartości skalarnej z DataFrame
print("Polars lazy mean:", mean_lazy)
print("Czas:", time.time() - start)

print(150*"=")
#dask
start = time.time()
df_dask = dd.read_csv(filename)
mean_dask = df_dask["value"].mean().compute()  # .compute() uruchamia obliczenia
print("Dask mean:", mean_dask)
print("Czas:", time.time() - start)