import pandas as pd

df =pd.read_csv("marketing_r.csv",
                sep=',',
                parse_dates=['date_served',
                             'date_subscribed',
                             'date_canceled'])

print(df.head())

# import pandas as pd
#
# df = pd.read_csv("marketing_r.csv", sep=',')
#
# date_cols = ['date_served', 'date_subscribed', 'date_canceled']
# for col in date_cols:
#     df[col] = pd.to_datetime(df[col], format='%Y-%m-%d', errors='coerce')  # podaj odpowiedni format daty
#
# print(df.head())
