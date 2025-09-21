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

# zmiana daty na typ datetime
df['date_served']=pd.to_datetime(df['date_served'], errors='coerce',format='mixed')
print(df.head(5).to_string())

df.info()
print(150*'=')

# dodanie kolumny channel_code, zmiana nazw marketing_channel na chanel_code
channel_dict = {"House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, "Push": 5}
df['channel_code']=df['marketing_channel'].map(channel_dict)
print(df.head(5).to_string())

df['day_name']=df['date_served'].dt.day_name()
print(df['day_name'].head(3))


#unikalni uzytkownicy dziennie

daily_user = df.groupby(['date_served'])['user_id'].nunique()
print("dziennie:", daily_user)


import matplotlib.pyplot as plt

daily_user.plot()
plt.title("Zasięg dzienny kampanii marketingowej")
plt.xlabel("Data")
plt.ylabel("Liczba użytkowników")
plt.xticks(rotation=60)
plt.show()