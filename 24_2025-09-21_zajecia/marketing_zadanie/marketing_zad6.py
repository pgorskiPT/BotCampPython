import  pandas as pd
import  matplotlib.pyplot as plt

df=pd.read_csv('marketing_ok_date.csv', sep=",")


def conversion_rate(dataframe, columns_names):
    columns_conv=dataframe[dataframe['converted']==True].groupby(columns_names)['user_id'].nunique()
    column_total=dataframe.groupby(columns_names)['user_id'].nunique()

    conversion_rate = columns_conv/column_total
    conversion_rate=conversion_rate.fillna(0)# NaN wypełni zerami

    return conversion_rate


def plotting_conv(dataframe):
    for column in dataframe:
        plt.plot(dataframe.index,dataframe[column])

        plt.title('Daily'+str(column)+"conversion rate\n", size=16)
        plt.ylabel('Conversion rate' , size=14 )
        plt.xlabel('Date', size=14)
        plt.xticks(rotation=45)
        plt.show()
        plt.clf() # czyści wykres


if __name__ == '__main__':
    age_group_conv=conversion_rate(df,['date_served',"age_group"])
    print(age_group_conv)

    age_group_conv_df=pd.DataFrame(age_group_conv.unstack(level=1))
    plotting_conv(age_group_conv_df)