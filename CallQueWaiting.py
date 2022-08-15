import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\JULYCDR\\cdr-010722.csv')
df1=df[df.Hour==19]
print(round(len(df1[(df1.Level=='Entry') &  (df1.FRL==2) & (df1.QueDuration <= 60)])/len(df1[(df1.Level=='Entry') & (df1.FRL==2)])*100,2))
print(len(df1[(df1.Level=='Second') &  (df1.FRL==2) & (df1.QueDuration <= 45)])/len(df1[(df1.Level=='Second') & (df1.FRL==2)])*100)
print(round(len(df1[(df1.Level=='Third') &  (df1.FRL==2) & (df1.QueDuration <= 30)])/len(df1[(df1.Level=='Third') & (df1.FRL==2)])*100,2))

