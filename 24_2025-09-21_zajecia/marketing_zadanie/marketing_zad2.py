import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_r.csv')
# print(df.head().to_string())
df = pd.read_csv('marketing_r.csv', sep=",")
# print(df.head(1).to_string())

# sprawdzmy jaki typ m kolumna 'converted'
print(df['converted'].dtype)  # object
print(150*'=')

df['is_house_ads'] = np.where(df['marketing_channel'] == "House Ads", True, False)
print(df.is_house_ads.head(3))
print(150*'=')

# zmienić typ kolumny na typ bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()

print(150*'=')

df['date_served'] = pd.to_datetime(df['date_served'], errors='coerce', format='mixed')
print(df['date_served'].head(3))
print(150*'=')

channel_dict = {"House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, "Push": 5}
df['channel_code'] = df['marketing_channel'].map(channel_dict)
print(df['channel_code'].head(3))
print(150*'=')

daily_users = df.groupby(['date_served'])['user_id'].nunique()
print("Dziennie:", daily_users)
print(150*'=')

df.info()
print(150*'=')
df.to_csv("marketing_ok_date.csv")


subscribers = df[df['converted'] == True]['user_id'].nunique()
total = df['user_id'].nunique()
print("Subscribers:", subscribers)
print("Total:", total)
# Subskrybenci: 1030
# Total: 7309
print(150*'=')

# współczynnik konwersji
conv_rate = subscribers / total
print("Convert rate:", conv_rate)  # Convert rate: 0.14092215077301956
print("Convert rate:", round(conv_rate * 100, 2), "%")  # Convert rate: 14.09 %
print(150*'=')


# wspolczynnik utrzymania użytkownika
retained = df[df["is_retained"] == True]['user_id'].nunique()
retention = retained / subscribers
print("Retention rate:", round(retention * 100, 2), "%")  # Retention rate: 65.83 %


print(150*'=')
# House Ads
house_ads = df[df['subscribing_channel'] == "House Ads"]
retained = house_ads[house_ads["is_retained"] == True]["user_id"].nunique()
subscribers = house_ads[house_ads['converted'] == True]['user_id'].nunique()
retention_rate = retained / subscribers
print("Retention rate:", round(retention_rate * 100, 2), "%")  # Retention rate: 58.05 %


print(150*'=')
retained=df[df['is_retained']==True].groupby(['subscribing_channel'])["user_id"].nunique()
print(retained)


print(150*'=')
subscribers=df[df['converted']==True].groupby(['subscribing_channel'])["user_id"].nunique()
print(subscribers)

print(150*'=')
chanel_retention_rate=(retained/subscribers)*100
print(chanel_retention_rate)