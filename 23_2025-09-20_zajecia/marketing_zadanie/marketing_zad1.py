import pandas as pd
import numpy as np

df= pd.read_csv('marketing_r.csv', sep=',')

print(df.describe())
print(150*'=')
print(df.head(2).to_string())
print(150*'=')
df.info()
print(150*'=')


#sprawdzmy jaki typ ma kolumna 'converted'
print(df['converted'].dtype)
df['converted'] = df['converted'].astype(bool)
print(df['converted'].dtype)
print(150*'=')
df.info()
print(150*'=')
print(df.head(5).to_string())
print(150*'=')

df['is_hause_ads']=np.where(df['marketing_channel']=="House Ads",True,False)
print(150*'=')
print(df.head(5).to_string())
print(150*'=')

df.to_csv("marketing_is_hause_ads.csv",sep=",", index=False)

df.info()
print(150*'=')