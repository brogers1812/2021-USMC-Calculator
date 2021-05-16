import os
import pandas as pd

#Determine validity of users age
def age():
    try:
        years = int(input("What is your age?:  "))
        if years < 17:
            print("You are too young to serve.")
            age()
        else:
            print("You are {} years old".format(years))
            return years
    except ValueError:
        print("Please input a numerical value.") 
        age()  


years = str(age())
print(years)

#Recieve total pulls from user
pullup = int(input("How many pullups?:  "))
if type(pullup) == int:
    print("You performed {} pullups".format(pullup))
else:
    print("That's not a valid response.")

pullup=str(pullup)
#print(type(pullup))
#print(pullup)



#read and setup male pullup CSV files
m_pullup_df=pd.read_csv("m_pull.csv",index_col=0)
m_pull_pts = m_pullup_df.loc[[pullup],[years]].values[0]


print(int(m_pull_pts))