import pandas as pd 

data = pd.read_csv('application/database.csv')
df = pd.DataFrame(data, columns = ['model','effect','year_intro','series'])
print(df)

