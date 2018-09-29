from random import choice
import string
def randomnum(length=10, chars=string.ascii_letters[0:54]+string.digits):
    from random import choice
    import string
    return ''.join([choice(chars) for i in range(length)])
def main(level):
    import os,time
    if level<3 and level>0:
        char = string.digits
    elif level<5 and level>2:
        char = string.ascii_letters[0:26]                   
    elif level<7 and level>4:
        char = string.ascii_letters[0:52]
    elif level<9 and level>6:
        char = string.ascii_letters[0:52]+string.digits
    else:
        char = string.ascii_letters[0:52]+string.digits+'#$%&\()*+-/:;<=>?@[\\]^_!~'
    code = randomnum(level+2,char)
    temp = open('temp.py','w')
    temp.write('import time\n')
    text = "print 'your code is : "+str(code)+"'"+'\n'
    temp.write(text)
    temp.write('time.sleep('+str(level+1)+')')
    os.startfile('temp.py')
    temp.close()
    time.sleep(0.5)
    os.remove('temp.py')
    return code
def playAgain():
    while True:
        try:
            print('-'*28,'<<QUARY>>','-'*28)
            ifplay = int(input('Enter 1 to play again and 0 to exit ... :'))
            if ifplay == 0:
                return False
            elif ifplay == 1:
                return True
            else:
                print('Please enter 0 or 1 ')
        except:
            print('please enter a Correct value!!')

def start():
    import time
    while True:
        try:
            level = int(input("\nEnter the Level number(1..10): "))
            
            if level>0 and level<11:
                break
            else:
                raise Exception("Error!")
        except:
            print("Please enter a correct Value !!")
    inp = input("\nAre you ready to get the code??..Press Enter to view it >>> ")
    code = main(level)
    print("\nWait for 5 seconds....>>\n")
    for i in range(level + 5):
        time.sleep(1)
        print('.', end=' ')

    ans = input("\n\nEnter the code now : ")
    if code == ans:
        score = level * 2
        print("\nYour memory is EXCELLENT!!")
        print("CONGRATULATIONS!!\n")
        print("your score is ",score)
        return score
    else:
        score = -1
        print("\nYour memory is very LOW!!")
        print("The code was",code,'\n')
        print("your score is ",score)
        return score

import time
print('You are going to play the MEMORY GAME....\n')
print('='*25,'<<GAME STARTS>>','='*25)
score = start()
total = score
played = 1
while playAgain():
    print('-'*25,'<<STARTING AGAIN>>','-'*25)
    score = start()
    total += score
    played += 1
else:
    print('\n','='*25,'<<GAME STOPPED>>','='*25)
    print('ANALYSIS:\n')
    print("You played",played,"times...")
    print("Your total score is",total)
    time.sleep(3)
