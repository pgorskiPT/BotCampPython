import  pandas as pd
import  matplotlib.pyplot as plt

df=pd.read_csv('marketing_ok_date.csv', sep=",")

language_age=df.groupby(['language_preferred', "age_group"])['user_id'].count()
language_age=pd.DataFrame(language_age.unstack(level=0))

print(language_age.head())


# language_age.plot(kind='bar', figsize=(12, 7))
# plt.title('Liczba użytkowników wg grupy wiekowej i preferowanego języka')
# plt.xlabel('Grupa wiekowa')
# plt.ylabel('Liczba użytkowników')
# plt.xticks(rotation=45)
# plt.legend(title='Język preferowany')
# plt.tight_layout()
# plt.show()


# language_age.plot(kind='line', figsize=(12, 7))
# plt.title('Liczba użytkowników wg grupy wiekowej i preferowanego języka')
# plt.xlabel('Grupa wiekowa')
# plt.ylabel('Liczba użytkowników')
# plt.xticks(rotation=45)
# plt.legend(title='Język preferowany')
# plt.tight_layout()
# plt.show()

language_age=df.groupby([ "age_group",'language_preferred'])['user_id'].count()
language_age=pd.DataFrame(language_age.unstack(level=0))

print(language_age.head())
language_age.plot(kind='bar', figsize=(12, 7))
plt.title('Liczba użytkowników wg grupy wiekowej i preferowanego języka')
plt.xlabel('Grupa wiekowa')
plt.ylabel('Liczba użytkowników')
plt.xticks(rotation=45)
plt.legend(loc="upper left",title='Język preferowany')
# plt.legend(loc="upper left",labels = language_age.columns.values)
plt.tight_layout()
plt.show()