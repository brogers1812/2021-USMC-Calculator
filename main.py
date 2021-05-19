#My first python scripts

import os
import pandas as pd

#Determine user gender
while True:
    sex = input("Are you a male or female (M or F)?:  ").lower()
    if sex == "m" or sex == "M":
        print("You are a male.")
        break
    elif sex == "f" or sex == "F":
        print("You are a female")
        break
    else:
        print("Please use one of the following repsonses.\n (M / m / F / f)")

#Determine validity of users age
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not a numerical value! Try again.")
            continue
        else:
            return userInput
            break

age = inputNumber("How old are you?:  ")

if (age < 17):
    print("You are too young to serve.")
    inputNumber("How old are you?:  ")
else:
    print("You are {} years old".format(age))

age=str(age)


#Determine qualification for altitude compensation
while True:
    alt = input("Do you perform your PFT in a zone located above 4,500 feet mean sea level? (Y,y,N,n):  ").lower()
    if alt == "y" or alt == "Y":
        print("You qualify for the altitude compensation chart.")
        break
    elif alt == "n" or alt == "N":
        print("You do not qualify for the altitude compensation chart.")
        break
    else:
        print("Please use one of the following repsonses.\n (Y / y / N / n)")

#Recieve total pulls from user
pullup = int(input("How many pullups?:  "))
if type(pullup) == int:
    print("You performed {} pullups".format(pullup))
else:
    print("That's not a valid response.")

pullup=str(pullup)


#Recieve total crunches from user
crunch = int(input("How many crunches?:  "))
if type(crunch) == int:
    print("You performed {} crunches".format(crunch))
else:
    print("That's not a valid response.")

crunch=str(crunch)


#Recieve run time from user
run = input("What was your runtime?:  ")
run = [character for character in run if character.isalnum()]
run = int("".join(run))
print(run)


if type(run) == int:
    print("You ran the 3 mile: {} ".format(run))
else:
    print("That's not a valid response.")

run=str(run)














































#read and setup male pullup CSV files
m_pullup_df=pd.read_csv("lookup_records\csv\m_pull.csv",index_col=0)
m_pull_pts = m_pullup_df.loc[[pullup],[age]].values[0]

print(int(m_pull_pts))



#read and setup male crunch CSV files
m_crunch_df=pd.read_csv("lookup_records\csv\m_crunch.csv",index_col=0)
m_crunch_pts = m_crunch_df.loc[[crunch],[age]].values[0]

print(int(m_crunch_pts))


#read and setup <4500ft runtime CSV files
m_run_no_alt_df=pd.read_csv("lookup_records\csv\m_run_no_alt.csv",index_col=0)
m_run_no_alt_pts = m_run_no_alt_df.loc[[run],[age]].values[0]

print(int(m_run_no_alt_pts))


total = int(m_crunch_pts) ++ int(m_crunch_pts) ++ int(m_run_no_alt_pts)

print("Your total score is {} out of 300.".format(total))


print(age)
print(sex)
print(pullup)
print(crunch)
print(total)