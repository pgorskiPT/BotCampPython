import pandas as pd

print(pd.__version__)
# 2.3.2
# Series - odworowuje kolumny

name_dict = {"name": ["Radek", "Tomek"]}
print(name_dict)

# {'name': ['Radek', 'Tomek']}
print("=" * 30)

a = [1, 2, 3]  # jednowymiarowe , jak kolumna

myvar = pd.Series(a) # to jest jeden kolumna

print(myvar)

# 0    1
# 1    2
# 2    3
# dtype: int64

print("=" * 30)

print(myvar[0])
# 1
print("=" * 30)

myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
# x    1
# y    2
# z    3
# dtype: int64
print("=" * 30)

print(myvar["y"])
# 2
print("=" * 30)
calories={'day1':420,"day2":380, "day3":390}
myvar=pd.Series(calories)
print(myvar)
# day1    420
# day2    380
# day3    390
# dtype: int64


print("=" * 30)


myvar=pd.Series(calories,index=["day1","day2"])
print(myvar)
# day1    420
# day2    380
# dtype: int64
print("=" * 30)

#DataFrame - odwzorowanie kolumny wiele kolumn czyli wiele Series
data={
    "calories":[420,380,390 ],
    "duration":[50,40,45]
}

df=pd.DataFrame(data)
print(df)

#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45

print("=" * 30)


print(df.loc[0])

# calories    420
# duration     50
# Name: 0, dtype: int64

print("=" * 30)

print(type(df.loc[0]))
# <class 'pandas.core.series.Series'>
print("=" * 30)

print(df.loc[[0,1]])
#    calories  duration
# 0       420        50
# 1       380        40


print("=" * 30)

print(type(df.loc[[0,1]]))
# <class 'pandas.core.frame.DataFrame'>

print("=" * 30)

df = pd.DataFrame(
    {
        "Name": [
            "Tomek",
            "Radek",
            "Zenek",
            "Anna"
        ],
        'Age': [22, 45, 35, 29],
        "Sex": ['male', 'male', 'female', 'female']
    }
)
print(df)

#     Name  Age     Sex
# 0  Tomek   22    male
# 1  Radek   45    male
# 2  Zenek   35  female
# 3   Anna   29  female

print("=" * 30)


print(df['Age'])

# 0    22
# 1    45
# 2    35
# 3    29
# Name: Age, dtype: int64

print("=" * 30)



# wyciągniecie maksymalnej wartości
print(df['Age'].max())  # 45

print("=" * 30)
print(df.describe())
#              Age
# count   4.000000
# mean   32.750000
# std     9.742518
# min    22.000000
# 25%    27.250000
# 50%    32.000000
# 75%    37.500000
# max    45.000000
print("=" * 30)
print(df.loc[0])
# Name    Tomek
# Age        22
# Sex      male
# Name: 0, dtype: object