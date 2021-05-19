from numpy import round_
import pandas as pd


age=str(35)


#crunch = int(input("How many crunches?:  "))
#if type(crunch) == int:
#    print("You performed {} crunches".format(crunch))
#else:
#    print("That's not a valid response.")
#
#crunch=str(crunch)
    


run = input("What was your runtime?:  ")
run = [character for character in run if character.isalnum()]
run = int("".join(run))

if(run % 10 !=0):
   run = (run - run % 10) + 10

if run 

print(run)



if type(run) == int:
    print("You ran the 3 mile: {} ".format(run))
else:
    print("That's not a valid response.")

run=str(run)


#read and setup <4500ft runtime CSV files
m_run_no_alt_df=pd.read_csv("lookup_records\csv\m_run_no_alt.csv",index_col=0)
m_run_no_alt_pts = m_run_no_alt_df.loc[[run],[age]].values[0]

print(int(m_run_no_alt_pts))

