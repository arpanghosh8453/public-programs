#----------------------------------imports--------------------------------------
import itertools,re,random,getpass
#----------------------------------Authentification-----------------------------
print "** Copyright : Arpan Ghosh ** \n"
print "This game is Programmed by Arpan Ghosh. All rights reserved .\n"
print "Verification : Enter the ",
password = getpass.getpass()
if hash(password) == -809589229:#MATCHING HASH PASSWORD VALUE
    print "\nAcess granted : Welcome to the Guess my number game !!\n"
else:
    print "\nError : Wrong password input...Sorry!\n"
    x = raw_input("Press Enter to exit!!")
    exit()

#---------------------------------COMPUTER BRAIN---------------------------------
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


#takes the number and the resulted symbols,
#return a lists of list of all possible right-position,wrong-position & not occuring values combinations altering their positions
#in serial => [[right_position,wrong_position,not_present].....]

#takes the number,resulted symbols,possible_value_list and sorts them with the values in master Expression list
#returns the list of numbers which passes through the checking
def sort_nums(guess,result,numbers):
    sorted_list = []
    for num in numbers:#iteretes through all numbers
        r_w_n = get_right_wrong_none(num,guess)#gets the symbolic values for itereting number
        if (r_w_n.count('r') == result.count('r') and r_w_n.count('w') == result.count('w')) and (r_w_n.count('-') == result.count('-')):#matches symbolic values
            sorted_list.append(num)#sorted values appends to the sorted_list
    return sorted_list


# checks whether the values are only occuring inside symbols
#returns false if any element of symbols is not in values
def check_errors(symbols,values):
    for i in symbols:
        if i not in values:
            return True
    else:
        return False

    
#-------------------------------------Computer Brain part ends--------------------------------------------
#function for making the guess of number by computer
def comp_guess(length,numbers):
    num = random.choice(numbers)
    step_count = 0
    while numbers != []:
        choice = random.choice(numbers)#choicing the number randomly from the possible available numbers
        while True:
            ask = get_right_wrong_none(num,choice)#getting the symbols from uesr
            #error checking in input
            if len(ask) != length or check_errors(ask,['w','r','-']):
                print "Please enter a valid value( r:right ; w:wrong ; -:not present)"
            else:
                break
        #leave the loop if the number is absolutely correct
        if ask == 'r'*length:
            break
        numbers = sort_nums(choice,ask,numbers)#sorting the possible values according to the recently found input and making them as possible available numbers
        step_count += 1
        #print numbers#(for printing numbers)

    if ask != 'r'*length:#error check if no possible number is left
        print "Your number cannot exist !! Computer wins !!"
    print step_count,',',
    
#---------------------------------------------------------------------------------------------------------------
length = int(raw_input("Enter the number length for self playing by computer : "))
print '\n'
for i in range(1000):
    data = range(10**(length-1),10**length)
    numbers =  filter(if_no_repeat,data)#discarding the numbers with repitition
    comp_guess(length,numbers)

x = raw_input("Enter to exit : ")#pause of program when it ends!
