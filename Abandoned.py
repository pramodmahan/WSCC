import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\JULYCDR\\cdr-010722.csv')
df1=df[df.FRL==0]
df2=df[df.FRL==2]
print("Total Calls   ",  len(df))
print("IVR Calls     ",  len(df1))
print("Agent Calls   ",  len(df2))
print("Short Calls   ",  len(df2[df2.AgentDuration < 10]))
print("Billable Calls",  len(df2[df2.AgentDuration >= 10]))
i=len(df[df.FRL==3])/len(df[(df.FRL==2) | (df.FRL==3)])
j=1-i
print("Abandoned Calls %" , i*100)
print("Answered Calls %",  j*100)