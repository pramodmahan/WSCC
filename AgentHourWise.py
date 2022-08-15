import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\JULYCDR\\cdr-010722.csv')
df1=df.groupby('AgentID').mean()
df2=df1[]
print(df2)