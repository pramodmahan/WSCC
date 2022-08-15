import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('C:\\Users\\lenovo\\Desktop\\Helio-1990.xlsx')
df.iloc[0,100].plot(kind ='line')
plt.show()