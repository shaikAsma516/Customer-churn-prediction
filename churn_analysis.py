import pandas as pd
df=pd.read_csv('customer_churn.csv')
churn_rate=(df['Churn'].eq('Yes').mean())*100
print('Churn Rate:', churn_rate)
print(df.groupby('Contract_Type')['Churn'].apply(lambda x:(x=='Yes').mean()*100))
