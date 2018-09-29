#-----------------------importing & defining globals------------------------------
import random,datetime,string,time
global totalscore
totalscore = 0
global timesPlayed
timesPlayed = 0
#--------------------------printing the introduction------------------------------
print('INSTRUCTIONS :')
print("a serize of random numbers will be given to you (according to your level choice) and you will be asked to find the count of a pariculler number...")
print('')
print('='*80)
print('Game starts :')
print('='*80)
print('')
#--------------------------defining functions------------------------------------
def randlist(length = 5,chars = string.digits):
    randlist = []
    for i in range(length):
        randnum = int(random.choice(chars))
        randlist.append(randnum)
    return randlist

def countfromlist(doublelist,num):
    count = 0
    for sublist in doublelist:
        for n in sublist:
            if n == num:
                count += 1
    return count
def printlist(doublelist):
    for sublist in doublelist:
        for num in sublist:
            print(num, end=' ')
        print('')

def createmainlist(length):
    mainlist = []
    for i in range(length):
        sublist = randlist(length)
        mainlist.append(sublist)
    return mainlist
def playAgain(): 
    while True:
        try:
            ifplay = int(input('enter 1 to play again and 0 to exit : '))
            if ifplay == 0:
                return False
            elif ifplay == 1:
                return True
            else:
                raise Exception('Error!')
        except:
            print('Please enter a valid value!') 
def checklength():
    while True:
        try:
            length = int(input('enter the level number(1..10):'))
            if type(length) is int:
                if length>10 or length<1:
                    raise Exception('Value Error!!')
                else:
                    return length
            else:
                raise Exception('Type Error!!')
        except:
             print('Please enter a valid value!') 
def checkanswer():
    while True:
        try:
            answer = int(input('Enter Your Answer please.. : '))
            if type(answer) is int:
                if answer>-1 and answer<10:
                    return answer
                else:
                    raise Exception('Value Error!!')
            else:
                raise Exception('Type Error!!')
        except:
            print('Please enter a valid value!')
#--------------------------defining the main function----------------------------
def main():
    global totalscore
    global timesPlayed
    while True:
        length = checklength()
        length = length + 3
        mainlist = createmainlist(length)
        selected = random.randint(0,9)
        printlist(mainlist)
        computercount = countfromlist(mainlist,selected)
        print('Question : count the number of '+str(selected)+' from the given box of numbers..')
        startTime = datetime.datetime.now()
        ans = checkanswer()
        endtime = datetime.datetime.now()
        timeTaken = (endtime-startTime)
        timesecond = timeTaken.seconds
        type(timesecond)
        if computercount == ans:
            print("That's CORRECT!!")
            print('Your game score :',(length/timesecond)*2)
            totalscore = totalscore + (length/timesecond)*2
        else:
            print("Wrong Answer!!")
            print("The correct answer is :",computercount)
            print('Your game score :',0)
        
        timesPlayed += 1
        print('Your total score :',totalscore)
        print('Time taken :',(timeTaken))
        if playAgain():
            print('-'*30, end=' ')
            print('STARTING AGAIN', end=' ')
            print('-'*30)
            pass
        else:
            print('Thanks for Playing!!')
            print('You played :',timesPlayed)
            print('your average :',float(totalscore)/timesPlayed)
            time.sleep(6)
            break
#-----------------------------calling the main function-------------------------------        
main()
    
    
