import sqlite3
import os
import pandas as pd 
conn = sqlite3.connect('upwork.db')

curr_dir = os.getcwd()

table_name = 'Upwork_Income'
folder_name = 'databases'
filename = 'income.csv'

attrib_list = ['Client', 'Total billed']

file_path = os.path.join(curr_dir,folder_name,filename)
df = pd.read_csv(file_path ,  names=attrib_list)

df.to_sql(table_name ,conn, if_exists='replace' ,index=False)
print('Table is ready')

# QUERY DATABSET

df2 = pd.read_sql(f'Select Count(*) As total_client from {table_name}',conn)
print(df2)

conn.close()