import pandas as pd 
data = [45,21,17,35,40,19,50,104,60]
df = pd.Series(data)

# To access the 3rd dataframe element
print(df[2])
# Access by position
print(df.iloc[2])
# print index range
print(df[1:4])
print(df.sort_values())

# Creating a DataFrame from a dictionary
data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David','AHSAN'],
        'Age': [25, 30, 35, 28,32],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago','Islamabad']}
df1 = pd.DataFrame(data1)
# fetch by column
print(df1['Name'].unique())
# Access second row
print(df1.iloc[2])
print(df1)

#write your code here
data = {'Student':['David','Samuel','Terry','Evan'],'Age':[27,24,22,32],'Country':['UK','Canada','China','USA'],'Course':['Python','Data Structures','Machine Learning','Web Development'],'Marks':[85,72,89,76]}
df = pd.DataFrame(data)
df
