#3번

#
import pandas as pd
import numpy as np


df1_data = np.ones((6, 7))
df1 = pd.DataFrame(df1_data, index=list('abcdef'), columns=list('ABCDEFG'))
df2_data = np.ones((7, 6))
df2 = pd.DataFrame(df2_data, index=list('abcdefg'), columns=list('ABCDEF'))
df3 = df1+df2


data = {'A': [np.nan, 3.0, 3.0, np.nan, np.nan, 2.0, np.nan],'B': [3.0, 3.0, 3.0, np.nan, np.nan, 2.0, np.nan],'C': [3.0, 3.0, 3.0, np.nan, np.nan, 2.0, np.nan],'D': [np.nan, np.nan, np.nan, np.nan, np.nan, 2.0, np.nan],'E': [np.nan, np.nan, np.nan, np.nan, np.nan, 2.0, np.nan],'F': [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, np.nan],'G': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]}
df3 = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(df3)
