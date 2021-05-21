#My first python script

import os
import pandas as pd

#Determine user gender
while True:
    sex = input("Are you a male or female (M or F)?:  ").lower()
    if sex == "m" or sex == "M":
        print("You are a male.")
        gender = "male"
        break
    elif sex == "f" or sex == "F":
        print("You are a female")
        gender = "female"
        break
    else:
        print("Please use one of the following repsonses.\n (M / m / F / f)")

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

#Determine pullups or pushup 
while True:
    pu = input("Did you perform pullups or pushups during your PFT? (1 = Pullup, 2 = Pushup):  ")
    if pu == "1":
        print("You selected pullups")
        break
    elif pu == "2":
        print("You selected pushups.")
        break
    else:
        print("Please use one of the following repsonses.\n (1 = Pullup, 2 = Pushup)")

if pu == "1":

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
        pull_pts = m_pullup_df.loc[[pullup],[age]].values[0]
        print(int(pull_pts))

    else:
    #read and setup female pullup CSV files
        f_pullup_df=pd.read_csv("lookup_records\csv\\f_pull.csv",index_col=0)
        pull_pts = f_pullup_df.loc[[pullup],[age]].values[0]
        print(int(pull_pts))

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
        pushup_pts = m_pushup_df.loc[[pushup],[age]].values[0]
        print(int(pushup_pts))

    else:
    #read and setup female pushup CSV files
        f_pushup_df=pd.read_csv("lookup_records\csv\\f_push.csv",index_col=0)
        push_pts = f_pushup_df.loc[[pushup],[age]].values[0]
        print(int(push_pts))
if pu == "1":
    pullup=int(pullup)
else:
    pushup_pts=int(push_pts)


#Recieve total crunches from user
crunch = int(input("How many crunches?:  "))
if type(crunch) == int:
    print("You performed {} crunches".format(crunch))
else:
    print("That's not a valid response.")

crunch=str(crunch)

if sex == "m":
    #read and setup male crunches CSV file
    m_crunch_df=pd.read_csv("lookup_records\csv\m_crunch.csv",index_col=0)
    crunch_pts = m_crunch_df.loc[[crunch],[age]].values[0]
    print(int(crunch_pts))

else:
    #read and setup female crunches CSV files
    f_crunch_df=pd.read_csv("lookup_records\csv\\f_crunch.csv",index_col=0)
    crunch_pts = f_crunch_df.loc[[crunch],[age]].values[0]
    print(int(crunch_pts))

crunch=int(crunch)

print

#Determine running or rowing 
while True:
    cardio = input("Did you perform a 3 mile run or 5000m row? (1 = Run, 2 = Row):  ")
    if cardio == "1":
        print("You selected the 3 mile run.")
        break
    elif cardio == "2":
        print("You selected the 5000m row.")
        break
    else:
        print("Please use one of the following repsonses.\n (1 = Run, 2 = Row)")

if cardio == "1":

    def inputRun(message):

        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not a numerical value! Please enter a four digit number. \n Example (2345, 2200, or 1923")
                continue
            else:
                return userInput
                break

#Recieve run time from user
    run = inputRun("What was your run time?")
    run = str(run)
    run = [character for character in run if character.isalnum()]
    run = int("".join(run))

    if(run % 10 !=0):
        run = (run - run % 10) + 10

    print(type(run))
    print("You ran the 3 mile: {} ".format(run))

    run=str(run)
    print(type(run))
    
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

else:

    def inputRow(message):

        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not a numerical value! Please enter a four digit number. \n Example (2345, 2200, or 1923")
                continue
            else:
                return userInput
                break

    #Recieve row time from user
    row = input("What was your row time?:  ")
    row = str(row)
    row = [character for character in row if character.isalnum()]
    row = int("".join(row))

    if(row % 5 !=0):
        row = (row - row % 5) + 5

    print(row)
    print("You rowed the 5000m: {} ".format(row))
    row=str(row)

    if alt == "n" and sex == "m":
        
        #read and setup <4500ft runtime for males CSV files
        m_row_no_alt_df=pd.read_csv("lookup_records\csv\\m_row_no_alt.csv",index_col=0)
        row_pts = m_row_no_alt_df.loc[[row],[age]].values[0]
        print(int(row_pts))

        #read and setup >4500ft rowtime for males CSV files
    elif alt =="y" and sex == "m":
        m_row_alt_df=pd.read_csv("lookup_records\csv\\m_row_alt.csv",index_col=0)
        row_pts = m_row_alt_df.loc[[row],[age]].values[0]
        print(int(row_pts))

        #read and setup <4500ft rowtime for females CSV files
    elif alt == "n" and sex == "f":    
        f_row_no_alt_df=pd.read_csv("lookup_records\csv\\f_row_no_alt.csv",index_col=0)
        row_pts = f_row_no_alt_df.loc[[row],[age]].values[0]
        print(int(row_pts))

        #read and setup >4500ft rowtime for females CSV files
    else:
        f_row_alt_df=pd.read_csv("lookup_records\csv\\f_row_alt.csv",index_col=0)
        row_pts = f_row_alt_df.loc[[row],[age]].values[0]
        print(int(row_pts))

os.system('cls')

print("You are {} years old".format(age))
print("You are a {}".format(gender))

#Print total pullup or pushup with score
try: pullup
except NameError: 
    print("You performed {} pushups for a score of {} points.".format(pushup, int(pushup_pts))) 
    event1 = pushup_pts
else:
    print("You performed {} pullups for a score of {} points.".format(pullup, int(pull_pts)))
    event1 = pull_pts

print("You performed {} crunches for a score of {} points.".format(crunch, int(crunch_pts)))
event2 = crunch_pts

#Display total run time or row time with score
try: run
except NameError: 
    print("You performed the 5000m run in {} for a score of {} points .".format(row, int(row_pts)))
    event3 = row_pts
else:
    print("You performed the 3 mile run in {} for a score of {} points.".format(run, int(run_pts)))
    event3 = run_pts

totalscore = int(event1 + event2 + event3)

if totalscore >= 235:
    pftclass = "first"
elif totalscore <= 235 and totalscore >= 200:
    pftclass = "second"
elif totalscore <=200 and totalscore >= 120:
    pftclass = "third"
else:
    pftclass = "Failed"
    print("Your total PFT score is {} out of 300 points.\nYou failed the PFT".format(int(totalscore)))

print("Your total PFT score is {} out of 300 points. \nYou earned a {} class PFT".format(int(totalscore), pftclass))

