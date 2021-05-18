#My first python scripts

import os
import pandas as pd

#Determine user gender
def gender():
    sex = str(input("Are you a male or female (M or F)?:  ")).lower()
    if sex == "m":
        print("You are a male.")
    elif sex == "f":
        print("You are a female")
    else:
        print("Please use one of the following repsonses.\n (M / m / F / f)")
        gender()  

gender()
gender = str(gender)
print(type(gender))

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

#Determine qualitification for altitude compensation
def altitude():
    alt = str(input("Do you perform your PFT in a zone located above 4,500 feet mean sea level? (Y,y,N,n):  ")).lower()
    if alt == "y":
        print("You qualify for the altitude compensation chart.")
    elif alt == "n":
        print("You do not qualify for the altitude compensation chart.")
    else:
        print("Please use one of the following repsonses.\n (Y / y / N / n)")
        altitude()  

altitude()
altitude = str(altitude)
print(type(altitude))

#Recieve total pulls from user
pullup = int(input("How many pullups?:  "))
if type(pullup) == int:
    print("You performed {} pullups".format(pullup))
else:
    print("That's not a valid response.")

pullup=str(pullup)

#read and setup male pullup CSV files
m_pullup_df=pd.read_csv("lookup_records\csv\m_pull.csv",index_col=0)
m_pull_pts = m_pullup_df.loc[[pullup],[years]].values[0]

print(int(m_pull_pts))

#Recieve total crunches from user
crunch = int(input("How many crunches?:  "))
if type(crunch) == int:
    print("You performed {} crunches".format(crunch))
else:
    print("That's not a valid response.")

crunch=str(crunch)

#read and setup male crunch CSV files
m_crunch_df=pd.read_csv("lookup_records\csv\m_crunch.csv",index_col=0)
m_crunch_pts = m_crunch_df.loc[[crunch],[years]].values[0]

print(int(m_crunch_pts))

total = int(m_crunch_pts) ++ int(m_crunch_pts)

print("Your total score is {} out of 300.".format(total))