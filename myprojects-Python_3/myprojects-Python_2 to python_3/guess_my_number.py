#-----------------------------------------------------------------imports----------------------------------------------------------------------------
import itertools,re,random,getpass
#-------------------------------------------------------------Authentification------------------------------------------------------------------------
print("** Copyright : Arpan Ghosh ** \n")
print("This number based game is Programmed by Arpan Ghosh. All rights reserved .\n")
print("Verification : Enter the ", end='')
password = getpass.getpass()
if password == 'arpan':#MATCHING HASH PASSWORD VALUE
    print("\nAcess granted : Welcome to the Guess my number game !!\n")
else:
    print("\nError : Wrong password input...Sorry!\n")
    x = input("**Press Enter to exit!!")
    exit()
#---------------------------------------------------------------INSTRUCTIONS--------------------------------------------------------------------------

instruction = '''-------------------------------INSTRUCTIONS------------------------------------
** This game is mainly based upon finding the guessed number by oppornent
as soon as possible.

** At first You have to decide the length of the number with which you are
going to play with computer.

** Some hints are provided to the player according to his/her/computer's
guessed number on the basis of the decided number by computer/player

                    ** hints are given as **

            * VALUE *                   * SYMBOL *
            
    right number & right position  ==>  Denoted by 'r'
    right number & wrong position  ==>  Denoted by 'w'
    number not present in guessed  ==>  Denoted by '-'

** There are options for playing both sides (e.g. deciding side & Guessing side)

                           HAVE FUN WITH THIS GAME.......
--------------------------------------------------------------------------------'''
enter = input("\nPress Enter to get Instruction for this game :")
print(instruction)
#---------------------------------------------------------------COMPUTER BRAIN------------------------------------------------------------------------
#Chechs whether there is any repeat in the given number
def if_no_repeat(num):
    for i in str(num):
        if str(num).count(i)>1:
            return False
    return True
#takes a list with same object mutiple occuring,returns another list without them
def sorter(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

#takes the number and the resulted symbols,
#return a lists of list of all possible right-position,wrong-position & not occuring values combinations altering their positions
#in serial => [[right_position,wrong_position,not_present].....]
def get_arrangement(num,result):
    all_data = []
    rearrenge_list = sorter(itertools.permutations(result))#makes the palmutation of the resulted symbols and sorts them
    for arrangement in rearrenge_list:
        expression = []
        
        not_present = ''
        inc = 0
        for value in arrangement:
            if value == '-':
                not_present += str(num)[inc]#sorting not present
            inc += 1
        
        wrong_position = ''
        inc = 0
        for value in arrangement:
            if value == 'w':
                wrong_position += str(num)[inc]#sorting wrong position
            inc += 1
        
        right_position = ''
        inc = 0
        for value in arrangement:
            if value == 'r':
                right_position += str(num)[inc]#sorting right position
            inc += 1
        data = [right_position,wrong_position,not_present]#values arranged according to one combination in serial
        if data not in all_data:
            all_data.append(data)#appending to the bigger master list
    return all_data#master list returned


#takes the number and the master list of all arrangement of right-position,wrong-position & not occuring values as input
#returns the all possible combinations as a list of regular expressions for possible numbers
def get_expression(num,all_arrangements):
    all_expression = []
    for arrangement in all_arrangements:#iterreting on master list of all possible right-position,wrong-position & not occuring value arrangement
        #extracting data from arrangement [right_position,wrong_position,not_present]
        correct = arrangement[0]
        wrong = arrangement[1]
        none = arrangement[2]
        
        none_wrong_arrange = list(wrong)+['[^'+none+']']*len(none)#making the format of regular expression for not occuring numbers and wrongly placed numbers
                                                                  #accordind to the working value of arrangement

        for arrange in sorter(itertools.permutations(none_wrong_arrange)):#makes the palmutation of the not present & wrongly placed values and sorts them
                                                                          #e.g. arranges them in every possible order
            expression = list(arrange)
            for i in correct:
                expression.insert(str(num).find(i),i)#inserting correct values to their respective correct positions
            #print arrange#(for printing arrange)
            for i in wrong:
                if str(num).find(i) == expression.index(i):
                    break # if the wrong is placed again in the wrong place it should not be included
            else:
                #print expression#(for printing expression)
                all_expression.append(expression)#appends the possible regular expression for possible numbers in master Expression list
                
    all_expression = sorter(all_expression)#sorts repitition
    
    return all_expression#returns master Expression list     

#combines the get_expression & get_arrangement
#takes the number,resulted symbols,possible_value_list and sorts them with the values of regular expression in master Expression list
#returns the list of numbers which passes through the regular expression checking
def sort_nums(num,result,sort_list):
    new_sorted_list = []
    exp_list = get_expression(num,get_arrangement(num,result))
    for number in sort_list:
        include = False
        for exp in exp_list:
            expression = ''.join(exp)
            match = re.match(expression,str(number))#matches with the re expression
            if match != None:
                include = True
                break
        if include == True:
            new_sorted_list.append(number)
    return new_sorted_list

# checks whether the values are only occuring inside symbols
#returns false if any element of symbols is not in values
def check_errors(symbols,values):
    for i in symbols:
        if i not in values:
            return True
    else:
        return False
#returns the appropiate symbols according to the given number and guessed number
#It randomizes the positions of them also
def get_right_wrong_none(number,guess):
    guess = str(guess)
    number = str(number)
    #error in input checking
    if if_no_repeat(guess) == False or len(number) != len(guess):
        raise ValueError("Wrong input")
    elif check_errors(str(number),['1','2','3','4','5','6','7','8','9','0']):
        raise ValueError("Wrong values")
    
    result = ''
    for i in guess:
        if i in number:
            if guess.find(i) == number.find(i):
                result += 'r'
            else:
                result += 'w'
        else:
            result += '-'
    result = list(result)
    random.shuffle(result)#for randomizing the resulted symbols
    return ''.join(result)
    

#function for making the guess of number by computer
def comp_guess(length,numbers):
    step_count = 0
    while numbers != []:
        choice = random.choice(numbers)#choicing the number randomly from the possible available numbers
        while True:
            ask = input('\nEnter a value for '+str(choice)+ " : ")#getting the symbols from uesr
            #error checking in input
            if len(ask) != length or check_errors(ask,['w','r','-']):
                print("\nPlease enter a valid value( r:right ; w:wrong ; -:not present)")
            else:
                break
        #leave the loop if the number is absolutely correct
        if ask == 'r'*length:
            break
        numbers = sort_nums(choice,ask,numbers)#sorting the possible values according to the recently found input and making them as possible available numbers
        step_count += 1
        #print numbers#(for printing numbers)

    if ask != 'r'*length:#error check if no possible number is left
        print("\nYour number cannot exist !! Computer wins !!")
    print("\ncomputer has won within ",step_count," Steps !! ")
    
#deciding the number by computer and takes input from user
#shows him/her the symbolic result by 'get_right_wrong_none' function
def man_guess(length,numbers):
    fair_game = False # the false value makes the game unfair by allowing computer to change the number dynamically
    downlimit = 0.5 # the limit under which computer tries to change its decided number if the game is unfair! 1 is the highest value for it,0 means fair game
    data = []
    comp_choice = random.choice(numbers)#random number choice
    step_count = 0
    result = None
    while result != 'r'*length:
        result = None
        while result == None:
            try:
                ask = input("\nEnter your guess : ")#taking the guess input from user
                step_count += 1
                result = get_right_wrong_none(comp_choice,ask)#getting the symbolic result
            #checking for error occurence
            except ValueError as error:
                print("\nYou must enter a valid guess .... !")
                #print error#(for error printing)
        prev_len = len(numbers)#storing previous length of possible values
        possible_list = sort_nums(ask,result,numbers)#getting a list of left possible values according to the given number and resulting symbols

        #tools for changing the decided number dynamically ( UNFAIR GAME PART )
        percent = len(possible_list)/float(prev_len)#finding the percent of retaintion of possibilities
        symbol_comb = sorter(itertools.combinations(['r']*length+['w']*length+['-']*length,length))#finding all possible combinations of symbols
        if percent<downlimit and not fair_game:#Unfairness starts if the left possibilities count percentage is below the downlimit
            symbols = []
            counts = []
            for comb in symbol_comb:
                comb = ''.join(comb)
                possible_values = sort_nums(ask,comb,numbers)#counting left possibilities for every possible symbol combinations
                if len(possible_values)/float(len(numbers)) >= downlimit:# for any symbol combination,if left possibilities percent rises over downlimit...
                    possible_list = list(possible_values)
                    comp_choice = random.choice(possible_list)
                    result = comb
                    break # Instantly make the combination as result and choice a suitable value from the left values , then exits the loop
                else:
                    symbols.append(comb)#otherwise makes a list of every possible combination vs. left possible values count
                    counts.append(len(possible_values))
            else:
                result = symbols[counts.index(max(counts))]#ultimately returns the value for maximum left possibilities if no value is upper than downlimit
                possible_list = sort_nums(ask,result,numbers)
                comp_choice = random.choice(possible_list)#makes a number choice accordingly the given result

        
        numbers = list(possible_list)#making the numbers as a list of left possible values
        #print numbers#(for printing numbers)
        data.append(ask+' : '+result)#making a list of 'numbers : results' datachart
        print('\n')
        for i in data:
            print(i)#printing datachart
        print('\n')
        #if the number is correctly guessed....
        if result == 'r'*length:
            print('\nYour guess is absolutely correct !! ')
            print('\nYou have won the match within',step_count,'steps !! ')
            break

#------------------------------------------------------------------Computer Brain part ends-------------------------------------------------------------------------
enter = input("Press Enter to start the game ...")
print("\n-----------------------------------Game Starts----------------------------------")
#getting the length Restriction of number guessing from user
length = int(input("\nEnter the length Restriction of number guessing (2..4) : "))
while length>4 or length<2:
    print("\nplease enter a length within 2 and 4 !! ")
    length = int(input("\nEnter the length Restriction of number guessing (2..4) : "))
#getting the player's playing side
player = input("\nEnter 1 : Computer will dacide the number and player will try to guess it\n\nEnter 2 : Player will decide the number and Computer will try to guess it\n\nEnter the Choice :")
#primary available numbers
data = list(range(10**(length-1),10**length))
numbers =  list(filter(if_no_repeat,data))#discarding the numbers with repitition
#control of changing player's side
print("\n--------------------------------------------------------------------------------")
if player == '1':
    man_guess(length,numbers)
elif player == '2':
    comp_guess(length,numbers)
else:
    pass
x = input("\nEnter to exit : ")#pause of program when it ends!

