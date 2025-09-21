import  pandas as pd
import  matplotlib.pyplot as plt

df=pd.read_csv('marketing_ok_date.csv', sep=",")

retention_total=df["user_id"].nunique()
print(retention_total)
print(150*'=')


retional_total=df.groupby(['date_subscribed', 'subscribing_channel'])['user_id'].nunique()
print(retional_total.head(3))

print(150*'=')

retention_subs=df[df['is_retained']==True].groupby(['date_subscribed','subscribing_channel'])['user_id'].nunique()
print(retention_subs.head(3))

print(150*'=')
retentin_rate=retention_subs/retional_total
print(retentin_rate.head(5))

print(150*'=')
retentin_rate=pd.DataFrame(retentin_rate.unstack(level=1))
# print(retentin_rate.head(5)) # 5 pierwszych wierszy
print(150*'=')
print(retentin_rate.tail(5)) # 5 ostanich  wierszy


retentin_rate.plot()
plt.title('Data zależności od kanału')
plt.xlabel('Data')
plt.ylabel('Użytkownicy')
plt.xticks(rotation=45)
plt.legend(title='Kanał')
plt.tight_layout()
plt.show()