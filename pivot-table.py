import pandas as pd

df = pd.read_excel('name of the excel file')
print(df)


df[['Gender', 'Product line', 'Total']]


pivot_table = df.pivot_table(index = 'Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
print(pivot_table)

#or

pivot_table.to_excel('pivot_table.xlsx','Report', startrow=4)