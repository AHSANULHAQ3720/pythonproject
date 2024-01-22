import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

df = pd.read_csv(filename)

# Print info about column with dtype

print(df.info())
# describe property

print(df.describe())

# Access random column

xlength = df[['Artist','Genre','Length']]
print(xlength)

# Access first row and first column

print(df.iloc[0,0])

# changing to new index
new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.index = new_index
df_new.loc['a','Artist']