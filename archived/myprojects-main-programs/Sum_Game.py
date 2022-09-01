from datetime import datetime
import time
def getnumber():
    from random import choice
    x = choice(range(30,80))
    y = choice(range(30,80))
    return x,y
def main():
    first,second = getnumber()
    prompt = str(first)+' + '+str(second)+" : "
    try:
        ans = int(raw_input(prompt))
        if ans == first+second:
            print "That's CORRECT!!"
            return 5
        else:
            print "WRONG answer!!"
            print "The correct answer is",first+second
            return -2
    except:
        print "Please enter a Correct value!!"
try:
    length = int(raw_input("Enter the total number of questions : "))
except:
    print "Please enter a Correct value!!"
totalScore = 0
start = datetime.now()
for i in range(length):
    score = main()
    totalScore += score
end = datetime.now()
print "\n","="*25,"<<ANALYSIS>>","="*25,"\n"
print "Time taken : ",(end-start)
print "Total Score : ",totalScore
print "\n","="*25,"<<THE END>>","="*25,"\n"
