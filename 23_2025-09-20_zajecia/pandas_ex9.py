import pandas as pd

df = pd.read_csv('data_with_date.csv')
print(df.to_string())


#sprawdzanie czy wiersze maja duplikaty w DataFrame
print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())

