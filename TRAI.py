import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\JULYCDR\\cdr-010722.csv')
print(len(df[(df.FRL==2) & (df.QueDuration <= 90)])/len(df[df.FRL==2])*100)

