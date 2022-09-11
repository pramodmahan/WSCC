import pandas as pd
df1 = pd.read_csv('C:\\Users\\localadmin\\Downloads\\cdr-090922.csv')
dfout = pd.read_excel('C:\\Users\\localadmin\\Downloads\\wscc-daily.xlsx')
df = df1.replace('Third', 'Entry')
df.loc[df["QueVDN"] == "AP_FRC_1503_TL_TEL_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_FRC_1503_TL_HIN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_FRC_1503_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1501_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1501_TL_HIN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1501_TL_KAN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1503_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1503_TL_HIN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_FRC_1503_TL_KAN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_TV_1507_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_TV_1507_TL_HIN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_TV_1507_TL_TEL_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "AP_TV_1507_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_TV_1507_TL_KAN_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_TV_1507_TL_ENG_SG", "Level"] = 'Third'
df.loc[df["QueVDN"] == "KA_TV_1507_TL_HIN_SG", "Level"] = 'Third'
dfAP = df[(df.Location == 'AndhraPradesh')]
dfKT = df[(df.Location == 'Karnataka')]
dfAP2 = dfAP[dfAP.AgentBillingCategory == 'Billable']
dfAP3 = dfAP2[dfAP2.Level != 'Third'].groupby(["Date", "CLI"])["CLI"].count().reset_index(name='count').sort_values(by=['Date', 'count'], ascending=[True, False])
dfAP4 = dfAP3[(dfAP3['count'] > 1)]
dfKT2 = dfKT[dfKT.AgentBillingCategory == 'Billable']
dfKT3 = dfKT2[dfKT2.Level != 'Third'].groupby(["Date", "CLI"])["CLI"].count().reset_index(name='count').sort_values(by=['Date', 'count'], ascending=[True, False])
dfKT4 = dfKT3[(dfKT3['count'] > 1)]
AP1 = dfAP.CLI.count()
AP2 = dfAP[dfAP.FRL == 0].CLI.count()
AP3 = dfAP[(dfAP.FRL == 2) | (dfAP.FRL == 3)].CLI.count()
AP4 = dfAP[dfAP.FRL == 2].CLI.count()
AP5 = round(AP4/AP3*100, 2)
AP6 = dfAP[dfAP.FRL == 3].CLI.count()
AP7 = round(AP6/AP3*100, 2)
AP8 = dfAP[(dfAP.FRL == 2) & (dfAP.QueDuration <= 90)].CLI.count()
AP9 = round(AP8/AP4*100, 2)
AP10 = dfAP4['count'].sum()-len(dfAP4)
KT1 = dfKT.CLI.count()
KT2 = dfKT[dfKT.FRL == 0].CLI.count()
KT3 = dfKT[(dfKT.FRL == 2) | (dfKT.FRL == 3)].CLI.count()
KT4 = dfKT[dfKT.FRL == 2].CLI.count()
KT5 = round(KT4/KT3*100, 2)
KT6 = dfKT[dfKT.FRL == 3].CLI.count()
KT7 = round(KT6/KT3*100, 2)
KT8 = dfKT[(dfKT.FRL == 2) & (dfKT.QueDuration <= 90)].CLI.count()
KT9 = round(KT8/KT4*100, 2)
KT10 = dfKT4['count'].sum()-len(dfKT4)
dfout.loc[0, 'A'] = AP1
dfout.loc[0, 'B'] = AP2
dfout.loc[0, 'C'] = AP3
dfout.loc[0, 'D'] = AP4
dfout.loc[0, 'E'] = AP5
dfout.loc[0, 'F'] = AP6
dfout.loc[0, 'G'] = AP7
dfout.loc[0, 'H'] = AP8
dfout.loc[0, 'I'] = AP9
dfout.loc[0, 'J'] = AP10
dfout.loc[0, 'K'] = round((AP10/AP8)*100)
dfout.loc[2, 'A'] = KT1
dfout.loc[2, 'B'] = KT2
dfout.loc[2, 'C'] = KT3
dfout.loc[2, 'D'] = KT4
dfout.loc[2, 'E'] = KT5
dfout.loc[2, 'F'] = KT6
dfout.loc[2, 'G'] = KT7
dfout.loc[2, 'H'] = KT8
dfout.loc[2, 'I'] = KT9
dfout.loc[2, 'J'] = KT10
dfout.loc[2, 'K'] = round((KT10/KT8)*100)
dfout.to_excel('C:\\Users\\localadmin\\Desktop\\wscc090922.xlsx')
