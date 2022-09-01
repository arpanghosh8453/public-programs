
def outputprint(l):
    for index in range(9):
        print(l[index], end=' ')
        if ((index+1) % 3) == 0:
            print('')

def changeinput1(l,step):
    while True:
        try:
            change1 = int(input("Enter a proper place number to print 'X':"))
            if (change1-1)in range(9) and l[change1-1] == '_':
                l[change1-1] = 'X'
                step += 1
                return step
                break
            else:
                print('Action cannot be performed!!')
        except: 
            print('please enter a Correct value!!')
def changeinput2(l,step):
    while True:
        try:
            change2 = int(input("Enter a proper place number to print '0':"))
            if (change2-1) in range(9) and l[change2-1] == '_':
                l[change2-1] = '0'
                step += 1
                return step
                break
            else:
                print('Action cannot be performed!!')
        except:
            print('please enter a Correct value!!')
def WonPlayer(l,firstPlayer,secondPlayer):
    if l[0] == l[1] == l[2] == 'X' or l[0] == l[1] == l[2] == '0':
        if l[0] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[3] == l[4] == l[5] == 'X' or l[3] == l[4] == l[5] == '0':
        if l[3] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[6] == l[7] == l[8] == 'X' or l[6] == l[7] == l[8] == '0':
        if l[6] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[0] == l[3] == l[6] == 'X' or l[0] == l[3] == l[6] == '0':
        if l[0] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[1] == l[4] == l[7] == 'X' or l[1] == l[4] == l[7] == '0':
        if l[1] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[2] == l[5] == l[8] == 'X' or l[2] == l[5] == l[8] == '0':
        if l[2] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[0] == l[4] == l[8] == 'X' or l[0] == l[4] == l[8] == '0':
        if l[0] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    elif l[2] == l[4] == l[6] == 'X' or l[2] == l[4] == l[6] == '0':
        if l[2] == 'X':
            return True,firstPlayer
        else:
            return True,secondPlayer
    else:
        return False,'None'
def PlayerInput():
    firstPlayer = input("Enter the first player name(team of 'X') :")
    secondPlayer = input("Enter the second player name(team of '0') :")
    return firstPlayer,secondPlayer
def win(player,step):
    print(player,'has WON the match with '+str(step)+' steps!!')
def draw(l):
    if '_' not in l:
        return True
    else:
        return False

def playAgain():
    while True:
        try:
            print('\n')
            ifplay = int(input('Enter 1 to play again and 0 to exit ... :'))
            if ifplay == 0:
                return False
            elif ifplay == 1:
                return True
            else:
                print('Please enter 0 or 1 ')
        except:
            print('please enter a Correct value!!')

def main():
    print('\n')
    print('='*25,'<<GAME STARTS>>','='*25)
    print('\n')
    firstPlayer,secondPlayer = PlayerInput()
    player1step = 0
    player2step = 0
    mainlist = list('_'*9)
    print('\n')
    outputprint(mainlist)
    while True:
        print('\n')
        print('Turn of '+firstPlayer+' ...')
        player1step = changeinput1(mainlist,player1step)
        print('Action Performed!!')
        print('\n')
        outputprint(mainlist)
        won,player = WonPlayer(mainlist,firstPlayer,secondPlayer)
        if won:
            print('\n')
            win(player,player1step)
            break
        elif draw(mainlist):
            print('\n')
            print('The game is draw!!')
            break
        print('\n')
        print('Turn of '+secondPlayer+' ...')
        player2step = changeinput2(mainlist,player2step)
        print('Action Performed!!')
        print('\n')
        outputprint(mainlist)
        won,player = WonPlayer(mainlist,firstPlayer,secondPlayer)
        if won:
            print('\n')
            win(player,player2step)
            break
        elif draw(mainlist):
            print('\n')
            print('The game is draw!!')
            break
    print('\n','Thanks for playing!!')
        
import time
print('you are going to play the ROUND-CROSS game....')
main()
while playAgain():
    main()
else:
    print('\n')
    print('='*25,'<<GAME STOPPED>>','='*25)
    print('\n')
    time.sleep(1)

    
