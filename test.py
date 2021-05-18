import os
import pandas as pd

reps = str(95)
years = str(17)

#read and setup male pullup CSV files
m_pullup_df=pd.read_csv("m_crunch.csv",index_col=0)
m_pull_pts = m_pullup_df.loc[[reps],[years]].values[0]


print(int(m_pull_pts))

#Recieve total crunches from user
crunch = int(input("How many crunches?:  "))
if type(crunch) == int:
    print("You performed {} crunches".format(crunch))
else:
    print("That's not a valid response.")

crunch=str(crunch)

#read and setup male crunch CSV files
m_crunch_df=pd.read_csv("m_crunch.csv",index_col=0)
m_crunch_pts = m_crunch_df.loc[[crunch],[years]].values[0]

print(int(m_crunch_pts))