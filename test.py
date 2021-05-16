import os
import pandas as pd

reps = str(17)
years = str(35)

#read and setup male pullup CSV files
m_pullup_df=pd.read_csv("m_pull.csv",index_col=0)
m_pull_pts = m_pullup_df.loc[[reps],[years]].values[0]


print(int(m_pull_pts))