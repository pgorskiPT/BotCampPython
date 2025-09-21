import pandas as pd

df=pd.read_csv('marketing_ok_date.csv', sep=",")

print(df.head(3))

print(150*'=')

language=df.groupby(["date_served", "language_preferred"])['user_id'].count()
print(language.head())


print(150*'=')
language=pd.DataFrame(language.unstack(level=1))
print(language.head())

import matplotlib.pyplot as plt

language.plot(kind='line', figsize=(10, 6))
plt.title("Dzienne preferencje jezykowe")
plt.ylabel('Liczba użytkowników')
plt.xlabel('Data')
plt.show()