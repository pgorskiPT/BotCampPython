import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("marketing_is_hause_ads.csv", sep=",")

print(df.head(3))
print(df["date_served"].dtype)

df['date_served']=pd.to_datetime(df['date_served'],format='%m/%d/%y')
print(df.head(3))
print(150 * '=')


email=df[df['marketing_channel']=='Email']
print(email.head().to_string() )

print(150 * '=')

alloc=email.groupby(['variant'])['user_id'].nunique()

print(alloc.head())
#
# alloc.plot(kind="bar")
# plt.title("Personalizacja tesktu")
# plt.ylabel("liczba")
# plt.show()
print(150 * '=')

subscribers=email.groupby(['user_id','variant'])['converted'].max()
print(subscribers.head() )

print(150 * '=')


subscribers_df=pd.DataFrame(subscribers.unstack(level=1))
control=subscribers_df['control'].dropna()
print(control.head())

print(150 * '=')
control.info()
print(150 * '=')


personalization=subscribers_df['personalization'].dropna()
print(personalization.tail())
print(150 * '=')


print("Control conversion rate:", np.mean(control))
print("Personalization conversion rate:", np.mean(personalization))


print(150 * '=')
import funkcjon_tools
print("Lift:",funkcjon_tools.lift(control, personalization))


def ab_segmentation(segment):
    for subsegment in np.unique(df[segment].values):
        print(subsegment)

    email=df[(df["marketing_channel"]=='Email')&(df[segment]==subsegment)]
    print(email.head().to_string())

    subscribers=email.groupby(['user_id','variant'])['converted'].max()
    print(subscribers.head())
    subscribers=pd.DataFrame(subscribers.unstack(level=1))
    control=subscribers['control'].dropna()

    personalization=subscribers['personalization'].dropna()
    print(control.dtype, personalization.dtype)

    print("Lift:", funkcjon_tools.lift(control,personalization))
    control=control.astype(int)
    personalization=personalization.astype(int)
    print("T-satic:",stats.ttest_ind(control, personalization) , "\n\n")


print(150 * '=')
ab_segmentation('language_displayed')
ab_segmentation("age_group")