import pandas as pd

df = pd.read_csv('C:\\Users\\lenovo\\Desktop\\JULYCDR\\cdr-010722.csv')
#print(df[(df.Level=='Entry') & (df.AgentDuration >= 10)].AgentDuration.mean())
#print(df[(df.Level=='Second') & (df.AgentDuration >= 10)].AgentDuration.mean())
#print(df[(df.Level=='Third') & (df.AgentDuration >= 10)].AgentDuration.mean())
#dfbool = df["CLI"].duplicated(keep='first')
#dfuni = df[~dfbool]
#dfdup = df[dfbool]
#dfdup.to_excel('C:\\Users\\lenovo\\Desktop\\dfdup.xlsx')
#uniquetime = dfuni.TotalTimeAtAgent.sum()
#Reptime = dfdup.TotalTimeAtAgent.sum()
#print(uniquetime)
#print(Reptime)
#print(uniquetime*1.15)
