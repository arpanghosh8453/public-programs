import random
numbers = [1,2,3,4,5,6,7,8,9]
def printer(l):
    print "\n","-"*25
    for number in range(81):
        print l[number],
        if number%3 == 2:
            print " ",
        if number%9 == 8:
            print ""
        if number%27 == 26:
            print "\n",
    print "-"*25
def makeBoard():
    board = None
    while board is None:
        board = attemptBoard()
    return board

def attemptBoard():
    board = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            checking = numbers[:]
            random.shuffle(checking)
            x = -1
            loopStart = 0
            while board[i][j] is None:
                x += 1
                if x == 9:
                    #No number is valid in this cell, start over
                    return None
                checkMe = [checking[x],True]
                if checkMe in board[i]:
                    #If it's already in this row
                    continue
                checkis = False
                for checkRow in board:
                    if checkRow[j] == checkMe:
                        #If it's already in this column
                        checkis = True
                if checkis: continue
                #Check if the number is elsewhere in this 3x3 grid based on where this is in the 3x3 grid
                if i % 3 == 1:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2]): continue
                elif i % 3 == 2:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2],board[i-2][j+1],board[i-2][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1],board[i-2][j-1],board[i-2][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2],board[i-2][j-1],board[i-2][j-2]): continue
                #If we've reached here, the number is valid.
                board[i][j] = checkMe
    return board


def printBoard(board):
    spacer = "++---+---+---++---+---+---++---+---+---++"
    print (spacer.replace('-','='))
    for i,line in enumerate(board):
        print ("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||".format(
                    line[0][0] if line[0][1] else ' ',
                    line[1][0] if line[1][1] else ' ',
                    line[2][0] if line[2][1] else ' ',
                    line[3][0] if line[3][1] else ' ',
                    line[4][0] if line[4][1] else ' ',
                    line[5][0] if line[5][1] else ' ',
                    line[6][0] if line[6][1] else ' ',
                    line[7][0] if line[7][1] else ' ',
                    line[8][0] if line[8][1] else ' ',))
        if (i+1) % 3 == 0: print(spacer.replace('-','='))
        else: print(spacer)

solvedlist = makeBoard()
mainlist = []
for index in solvedlist:
	for listpart in index:
		mainlist.append(listpart[0])
printer(mainlist)
printBoard(solvedlist)
x = raw_input("END")