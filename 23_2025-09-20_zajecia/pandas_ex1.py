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

