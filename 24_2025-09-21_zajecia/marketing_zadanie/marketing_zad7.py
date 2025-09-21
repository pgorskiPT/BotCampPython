import marketing_zad6 as fun
import pandas as pd

df = pd.read_csv("marketing_ok_date.csv", sep=",")

print(df.head(3))
print(df['date_served'].dtype)  # object

df['date_served'] = pd.to_datetime(df['date_served'], format='%Y-%m-%d')

print(df.head(3))
print(df['date_served'].dtype)  # object

house_ads = df[df['subscribing_channel'] == "House Ads"]
print(house_ads.head(3))

house_ads_b = house_ads[house_ads['date_served'] < '2018-01-11']
print(house_ads_b)
lang_conv = fun.conversion_rate(house_ads_b, ['language_displayed'])
print("lang_conv:\n", lang_conv)

spanish_index = lang_conv['Spanish'] / lang_conv['English']
arabic_index = lang_conv['Arabic'] / lang_conv['English']
german_index = lang_conv['German'] / lang_conv['English']
print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)

converted = (house_ads.groupby(['date_served', 'language_preferred'])
             .agg({"user_id": "nunique", "converted": "sum"}))
print(converted.head(3))
# unique - zwraca unikalne
# nunique - zwraca liczbe unikalnych

converted = pd.DataFrame(converted.unstack(level=1))
print(converted.head(3))

converted['english_conv_rate'] = (converted.loc['2018-01-11':"2018-01-31"][('converted', 'English')] /
                                  converted.loc['2018-01-11':"2018-01-31"][('user_id', 'English')])

print(converted.head(5))
print(150 * '=')
converted['expected_spanish_rate'] = converted['english_conv_rate'] * spanish_index
converted['expected_arabic_rate'] = converted['english_conv_rate'] * arabic_index
converted['expected_german_rate'] = converted['english_conv_rate'] * german_index

print(converted['expected_spanish_rate'])
print(150 * '=')
# print(converted['expected_arabic_rate'])
# print(150*'=')
# print(converted['expected_german_rate'])
# print(150*'=')

converted['expected_spanish_rate'] = converted['expected_spanish_rate'] * converted[("user_id", 'Spanish')]
converted['expected_arabic_rate'] = converted['expected_arabic_rate'] * converted[("user_id", 'Arabic')]
converted['expected_german_rate'] = converted['expected_german_rate'] * converted[("user_id", 'German')]
print(converted['expected_spanish_rate'].head(3))
print(150 * '=')

converted = converted.loc['2018-01-11':'2018-01-31']
expected_subs = (converted['expected_spanish_rate'].sum() +
                 converted['expected_arabic_rate'].sum() +
                 converted['expected_german_rate'].sum())
print("Exepcted:", expected_subs)

print(150 * '=')

actual_subs = (
        converted[('converted', 'Spanish')].sum()
        + converted[('converted', 'Arabic')].sum()
        + converted[('converted', 'German')].sum()
)
print("Actual sum:", actual_subs)

print(150 * '=')

actual_subs = sum([
    converted[('converted', 'Spanish')].sum(),
    converted[('converted', 'Arabic')].sum(),
    converted[('converted', 'German')].sum(),
])
print("Actual sum:", actual_subs)
print(150 * '=')


lost = expected_subs - actual_subs
print("Lost sum:", lost)
