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
print(sex)

#Determine users age
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
    age = inputNumber("How old are you?:  ")
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

print(alt)

#Determine pullups or pushup 
while True:
    alt = input("Did you perform pullups or pushups during your PFT? (1 = Pullup, 2 = Pushup):  ").lower()
    if alt == "1":
        print("You selected pullups")
        break
    elif alt == "2":
        print("You selected pushups.")
        break
    else:
        print("Please use one of the following repsonses.\n (1 = Pullup, 2 = Pushup)")

print(alt)

if alt == "1":

    #Recieve total pullups from user
    def inputPull(message):

        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not a numerical value! Try again.")
                continue
            else:
                return userInput
                break

    pullup = inputPull("How many pullups did you perform?")
    pullup = str(pullup)

    if sex == "m":
    #read and setup male pullup CSV file
        m_pullup_df=pd.read_csv("lookup_records\csv\m_pull.csv",index_col=0)
        m_pull_pts = m_pullup_df.loc[[pullup],[age]].values[0]
        print(int(m_pull_pts))

    else:
    #read and setup female pullup CSV files
        f_pullup_df=pd.read_csv("lookup_records\csv\\f_pull.csv",index_col=0)
        f_pull_pts = f_pullup_df.loc[[pullup],[age]].values[0]
        print(int(f_pull_pts))

    #Receive total pushups from user
else:
    def inputPush(message):

        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not a numerical value! Try again.")
                continue
            else:
                return userInput
                break

    pushup = inputPush("How many pushups did you perform?")
    pushup = str(pushup)  

    if sex == "m":
    #read and setup male pushup CSV file
        m_pushup_df=pd.read_csv("lookup_records\csv\m_push.csv",index_col=0)
        m_pushup_pts = m_pushup_df.loc[[pushup],[age]].values[0]
        print(int(m_pushup_pts))

    else:
    #read and setup female pullup CSV files
        f_pushup_df=pd.read_csv("lookup_records\csv\\f_pull.csv",index_col=0)
        f_push_pts = f_pushup_df.loc[[pushup],[age]].values[0]
        print(int(f_push_pts))


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

if(run % 10 !=0):
   run = (run - run % 10) + 10

print(run)

if type(run) == int:
    print("You ran the 3 mile: {} ".format(run))
else:
    print("That's not a valid response.")

run=str(run)

if alt == "n" and sex == "m":
    
    #read and setup <4500ft runtime for males CSV files
    m_run_no_alt_df=pd.read_csv("lookup_records\csv\\m_run_no_alt.csv",index_col=0)
    run_pts = m_run_no_alt_df.loc[[run],[age]].values[0]
    print(int(run_pts))

    #read and setup >4500ft runtime for males CSV files
elif alt =="y" and sex == "m":
    m_run_alt_df=pd.read_csv("lookup_records\csv\\m_run_alt.csv",index_col=0)
    run_pts = m_run_alt_df.loc[[run],[age]].values[0]
    print(int(run_pts))

    #read and setup <4500ft runtime for females CSV files
elif alt == "n" and sex == "f":    
    f_run_no_alt_df=pd.read_csv("lookup_records\csv\\f_run_no_alt.csv",index_col=0)
    run_pts = f_run_no_alt_df.loc[[run],[age]].values[0]
    print(int(run_pts))

    #read and setup >4500ft runtime for females CSV files
else:
    f_run_alt_df=pd.read_csv("lookup_records\csv\\f_run_alt.csv",index_col=0)
    run_pts = f_run_alt_df.loc[[run],[age]].values[0]
    print(int(run_pts))






#read and setup male crunch CSV files
m_crunch_df=pd.read_csv("lookup_records\csv\m_crunch.csv",index_col=0)
m_crunch_pts = m_crunch_df.loc[[crunch],[age]].values[0]

print(int(m_crunch_pts))



total = int(m_crunch_pts) ++ int(run_pts) 

print("Your total score is {} out of 300.".format(total))


print(age)
print(sex)
#print(pullup)
print(crunch)
print(run)
print(run_pts)
print(total)