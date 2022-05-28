import pandas as pd
from pyparsing import col


police=pd.read_csv('data.csv')
#print(police)


#for data cleaning remove column that only contains missing values
#df.isnull().sum()
#df.drop(columns=columnName, inplace=True)


#print(police.isnull().sum())
police2=police.drop(columns='country_name', inplace=True)
#print(police2)
#print(police)



#based on filtering and value counts

print(police.head(2))
police3=police[police.violation=='Speeding'].driver_gender.value_counts()
print(police3)



#gender affect who gets search during stop

print(police.groupby('driver_gender').search_conducted.sum())


print(police.search_conducted.value_counts())


#what is the mean stop duration
police4=police['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min':45})
print(police4)

#compare the age distribution for each violation

#police.groupby(col1).col2.describe()

print(police.groupby('violation').driver_age.describe())
