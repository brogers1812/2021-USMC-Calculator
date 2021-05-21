totalscore = int(input("Enter score"))

if totalscore >= 235:
    pftclass = "First Class"
elif totalscore <= 235 and totalscore >= 200:
    pftclass = "Second Class"
elif totalscore <=200 and totalscore >= 120:
    pftclass = "Third Class"
else:
    pftclass = "Failed"

print(pftclass)