import time
import dask.dataframe as dd
import  pandas as pd
import polars as pl


filename = "bigfile_polars.csv"


print(150*"=")
# pandas
start=time.time()
df=pd.read_csv(filename)
result=df.groupby("category")['value'].sum()
print("Pandas mean:", result)
print("Czas:", time.time()-start)


print(150*"=")
# polars
start=time.time()
df=pl.read_csv(filename)
result=df.group_by("category").agg(pl.col("value").sum())
print("Polars mean:", result.to_pandas())
print("Czas:", time.time()-start)


print(150*"=")
# polars lazy, scan
start = time.time()
df_lazy = pl.scan_csv(filename)
result=df_lazy.group_by("category").agg(pl.col("value").sum()).collect()
print("Polars lazy mean:", result.to_pandas())
print("Czas:", time.time() - start)


print(150*"=")
#dask
start = time.time()
df_dask = dd.read_csv(filename)
result_dask =df_dask.groupby("category")["value"].sum().compute()
print("Dask mean:", result_dask)
print("Czas:", time.time() - start)