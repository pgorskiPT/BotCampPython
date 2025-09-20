import pandas as pd

df= pd.read_csv('marketing_przecinek.csv', sep=',', nrows=1)
print(df)
print(150*'=')
print(df.columns)
df.columns =df.columns.str.replace(" ","")
print(150*'=')
# df_new=df.copy()
# print(df_new)

lista_kolumn=df.columns.tolist()
print(lista_kolumn)

df = pd.read_csv(
    'marketing_przecinek.csv',
    sep=r"\s{2,}",       # regex: minimum 2 białe znaki (spacje lub tabulatory)
    engine="python",     # konieczne dla regex separatora
    skiprows=1,          # poprawiona literówka
    header=None,
    names=lista_kolumn
)


print(df.head())
print(df.head(2).to_string())

df.to_csv("marketing_r.csv", sep=",", index=False)
# df.to_excel('fix3.xlsx',index=False)