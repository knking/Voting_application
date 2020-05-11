import random
no_of_can=int(input("Enter Number of candidates : "))
candidate=input(f'Enter {no_of_can} candidates Name With Space : \n').split()
print("Candidates are :-> ",candidate)
print("Voting is Going On ...... Please wait for the Results...")
print("Voting is Finishid.. And wait is Over")
print("Here are the results")

vots=[]

for k in range(0,no_of_can):
    c=random.randrange(1,100,3)
    vots.append(c)

for n in range(no_of_can):
    print(candidate[n]," Total Votes", ":",vots[n])

print("Hence The Winner is ....")
maximum=max(vots)
count=0
for r in range(no_of_can):
    if vots[r]==maximum:
        count =r
print(candidate[count],"Who Got Total ",":",maximum,"Votes")
