import numpy as np
import random,datetime
# *Inside the code, everywhere 0 is used as a starting index . but during result printing , 1 is considered as starting index.*
COUNT = 4  # No of similar Id should be matched to win the match.


# Returns True when the bottom point of the given point is filled(not blank) or when it is the bottommost point
# returns False if bottom point of the given point is blank
def is_filled_below(array, point):
    if point[0] == row_count-1:  # Checking for bottommost point
        return True
    if array[point[0]+1, point[1]] == 'x' or array[point[0]+1, point[1]] == '0':  # Checking for filled bottom point
        return True
    else:
        return False


# Returns the list of previous and later three(Count-4 = 3) points of the given point
# along /(left) diagonal direction maintaining the order top to bottom
def get_left_diagonal(array, point):
    left_diagonal = []
    for i in range(COUNT-1, -COUNT, -1):  # [3,2,1,0,-1,-2,-3] for COUNT = 4
        try:
            row, col = point[0]-i, point[1]+i  # getting left diagonal points top to bottom
            if row >= 0 and col >= 0 and (row, col) != point:  # to avoid inclusion of the point under checking
                value = array[row, col]
                if value == '.' and is_filled_below(array, (row, col)) is True:  # Replacing '.' with '?' if below point is filled
                    value = '?'
                left_diagonal.append(value)  
        except IndexError:  # suspend error raising for invalid points
            pass
    return left_diagonal


# Returns the list of previous and later three(Count-4 = 3) points of the given point
# along \(right) diagonal direction maintaining the order top to bottom
def get_right_diagonal(array, point):
    right_diagonal = []
    for i in range(COUNT-1, -COUNT, -1):  # [3,2,1,0,-1,-2,-3] for COUNT = 4
        try:
            row, col = point[0]-i, point[1]-i  # getting right diagonal points top to bottom
            if row >= 0 and col >= 0 and (row, col) != point:  # to avoid inclusion of the point under checking
                value = array[row, col]
                if value == '.' and is_filled_below(array, (row, col)) is True:  # Replacing '.' with '?' if below point is filled
                    value = '?'
                right_diagonal.append(value) 
        except IndexError:  # suspend error raising for invalid points
            pass
    return right_diagonal


# Returns the list of previous and later three(Count-4 = 3) points of the given point
# along |(vertical or upper-lower) direction maintaining the order top to bottom
def get_upper_lower(array, point):
    upper_lower = []
    for i in range(COUNT-1, -COUNT, -1):  # [3,2,1,0,-1,-2,-3] for COUNT = 4
        try:
            row, col = point[0]-i, point[1]   # getting vertical or upper-lower points top to bottom
            if row >= 0 and col >= 0 and (row, col) != point:  # to avoid inclusion of the point under checking
                value = array[row, col]
                if value == '.' and is_filled_below(array, (row, col)) is True:  # Replacing '.' with '?' if below point is filled
                    value = '?'
                upper_lower.append(value)
        except IndexError:  # suspend error raising for invalid points
            pass
    return upper_lower


# Returns the list of previous and later three(Count-4 = 3) points of the given point
# along ---(Horizontal or left-right) direction maintaining the order top to bottom
def get_left_right(array, point):
    left_right = []
    for i in range(COUNT-1, -COUNT, -1):  # [3,2,1,0,-1,-2,-3] for COUNT = 4
        try:
            row, col = point[0], point[1]-i  # getting Horizontal or left-right points top to bottom
            if row >= 0 and col >= 0 and (row, col) != point:  # to avoid inclusion of the point under checking
                value = array[row, col]
                if value == '.' and is_filled_below(array, (row, col)) is True:  # Replacing '.' with '?' if below point is filled
                    value = '?'
                left_right.append(value)
        except IndexError:  # suspend error raising for invalid points
            pass
    return left_right


# Creates a list of sub-lists containing three(Count-1 = 3) consecutive elements from the given list
# e.g. [1,2,3,4,5,6] ==> [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
def break_group(l):
    all_group = []  # list containing sub-lists
    length = len(l)
    for i in range(length-COUNT+2):
        sub_list = []
        for j in range(COUNT-1):
            sub_list.append(l[i+j])  # adding values in sub-list
        all_group.append(sub_list)
    return all_group


# returns a dictionary of ['left_diagonal','right_diagonal','upper_lower','left_right'] after passing through break_group.
# contains all the possible combination(as a group of three) of effective neighbouring points around given point of array.
def get_all_group(array, point):
    return {'left_diagonal': break_group(get_left_diagonal(array, point)), 
            'right_diagonal': break_group(get_right_diagonal(array, point)), 
            'upper_lower': break_group(get_upper_lower(array, point)), 
            'left_right': break_group(get_left_right(array, point))}


# generates the priority score of a point(According to it's neighbours) in the array with the help of all_group function
# '.' denotes a blank point whose bottom point is still blank(not filled)
# '?' denotes a blank point whose bottom point is filled.
def get_point_priority(array, point, char):
    group_dict = get_all_group(array, point)
    if char == '0':  # Score definition of all possible combinations for triplet neighbouring values
        # if the point under consideration is assumed to have Player Id '0'
        priority_dict = {
         ('.', '.', '.'): 0, 
         ('.', '.', '0'): 12, 
         ('.', '.', '?'): 4, 
         ('.', '.', 'x'): 2, 
         ('.', '0', '0'): 210, 
         ('.', '0', '?'): 18, 
         ('.', '0', 'x'): 1, 
         ('.', '?', '?'): 8, 
         ('.', '?', 'x'): 4, 
         ('.', 'x', 'x'): 24, 
         ('0', '0', '0'): 80001, 
         ('0', '0', '?'): 1000, 
         ('0', '0', 'x'): 4, 
         ('0', '?', '?'): 25, 
         ('0', '?', 'x'): 2, 
         ('0', 'x', 'x'): 1, 
         ('?', '?', '?'): 15, 
         ('?', '?', 'x'): 8, 
         ('?', 'x', 'x'): 220, 
         ('x', 'x', 'x'): 5000
        }
    else:
        # if the point under consideration is assumed to have Player Id 'x'
        priority_dict = {
         ('.', '.', '.'): 0, 
         ('.', '.', '0'): 2, 
         ('.', '.', '?'): 4, 
         ('.', '.', 'x'): 12, 
         ('.', '0', '0'): 24, 
         ('.', '0', '?'): 4, 
         ('.', '0', 'x'): 1, 
         ('.', '?', '?'): 8, 
         ('.', '?', 'x'): 18, 
         ('.', 'x', 'x'): 210, 
         ('0', '0', '0'): 5000, 
         ('0', '0', '?'): 210, 
         ('0', '0', 'x'): 1, 
         ('0', '?', '?'): 8, 
         ('0', '?', 'x'): 2, 
         ('0', 'x', 'x'): 4, 
         ('?', '?', '?'): 15, 
         ('?', '?', 'x'): 25, 
         ('?', 'x', 'x'): 1000, 
         ('x', 'x', 'x'): 80001
        }
    sum_value = 0  # Total overall priority or score of the point under consideration
    for key in group_dict.keys():
        for group in group_dict[key]:
                group.sort()  # Sorting is required to match actual order of 'priority_dict' keys in order => ['.','0','?','x']
                priority_dict_key = tuple(group)  # for matching the keys used in 'priority_dict'
                sum_value += priority_dict[priority_dict_key]  # adding priority or score to 'sum_value'
    return sum_value


# returns topmost vacant row value of given column
def get_fall_point(array, column):
    column_array = array.T[column]
    try:
        row = (len(column_array)-list(column_array)[::-1].index('.'))-1
    except:  # handle the error if the column has no vacancy on its top (Complete filled condition)
        row = -1  # IMPOSSIBLE ==> indicates Complete filled condition
    return row, column


# adds the given character ID in the topmost vacant point of the given column
def add(array, char, column):
    if column not in range(0,column_count):
        raise IndexError("Given column does not exists !")
    row, column = get_fall_point(array, column)  # gets topmost vacant row value of given column
    if row == -1:  # raise error if the column has no vacancy on its top (Complete filled condition)
        raise TypeError("the column is filled !")
    array[row, column] = char  # appends the given char in the topmost vacant point of the given column of given array


# Prints the array as game box shape
def print_box(array):
    print('\n ', end='')
    count = len(array[0])
    for i in range(1, count+1):
        print('', i, ' '*(2 - len(str(i))), end='')
    print('')
    for row in array:
        print('|', end='')
        for element in row:
            print(' '+str(element)+' |', end='')
        print('\n', end='')
    print('-'*(4*len(array[0])+1))


# Checks whether the player has just matched four(3+1) same player ID (requirement to win the game)
def has_won(array, point, char):
    group_dict = get_all_group(array, point)
    group_flat_list = []
    for key in group_dict.keys():
        for group in group_dict[key]:
            group_flat_list.append(group)
    if ([char]*(COUNT-1) in group_flat_list) and (array[point] == char):  # given point ID matched with same triplet(4-1) ID around it
        return True                                                         # Horizontally , vertically or diagonal groups
    else:
        return False


# Finds priority scores for all available fall points of each column
def get_target_point_scores(array, char):
    score_array = []  # list for storing priority score of each column sequentially .
    for i in range(column_count):
        fall_point = get_fall_point(array, i)  # get fall point of that column
        if fall_point[0] < 0 or fall_point[1] < 0:  # No fall point available for that column ( Completely filled )
            score_array.append(-100000)  # High negative score to avoid its selection
        else:
            score_array.append(get_point_priority(array, fall_point, char))  # adding the priority scores for
    return score_array                                                       # all available fall points of each column


# Finds priority scores for all cells just upper of all available fall points of each column
def get_upper_point_scores(array, char):
    score_array = []  # list for storing priority score of each column sequentially .
    for i in range(column_count):
        upper_point = (get_fall_point(array, i)[0]-1, get_fall_point(array, i)[1])  # get point upper to fall point of that column
        try:  # upper point of topmost points will not exist.
            score_array.append(get_point_priority(array, upper_point, char))  # adding the priority scores for
        except:                                              # all available points upper to fall points of each column
            score_array.append(0)  # no score(zero) to non-existing upper cells
    return score_array


# Choose the column according to the values of target_score_list and upper_score_list with the help of chooser function
def choose_column(array, char):
    target_score_list = get_target_point_scores(array, char)  # gets the target_score_list
    upper_score_list = get_upper_point_scores(array, char)  # gets the upper_score_list
    diff_list = (np.array(upper_score_list)-np.array(target_score_list)).tolist()  # difference of target_score_list and upper_score_list
    # print(target_score_list)  # for debugging
    # print(diff_list)  # for debugging
    return chooser(target_score_list, diff_list)  # chooses the most suitable column value


# chooses the suitable column based on target_score_list and diff_score_list values
# looks for most valuable column which has least losing value just upper to it as giving turn to the column
# exposes the upper point of the same column to opposite player
def chooser(target_score_list, diff_score_list):
    sorted_id_list = []
    choice_id = target_score_list.index(max(target_score_list))  # initial choice highest target_score column
    choice_value = target_score_list[choice_id]  # initial choice highest target_score value
    choice_diff = diff_score_list[choice_id]  # initial choice highest target_score value's difference value
    sorted_target_list = list(target_score_list)  # making a copy of target_score_list
    sorted_target_list.sort()  # sorting smaller to greater
    sorted_target_list = sorted_target_list[::-1]   # sorting greater to smaller

    for current_value in sorted_target_list:  # iterating through sorted_target_list
        current_id = target_score_list.index(current_value)
        current_diff = diff_score_list[current_id]
        if choice_diff >= 0:  # if chosen target_score value's difference value is positive => positive loss
            # if losing a small value, we can save later bigger loss , we should take that loss granted
            if (choice_value - current_value)*(5+(choice_value - current_value)/30) <= (choice_diff-current_diff):
                # if future gain is more than five+delta times of current loss....
                choice_id = current_id  # current choice ID should be changed to that current ID
                choice_value = current_value  # current choice value  be changed to that current value
                choice_diff = current_diff  # current choice diff  be changed to that current diff
                sorted_id_list = []  # sorted ID list should be renewed
        # small Randomization to avoid same choice in same condition every time
        if choice_value - current_value <= 20 and (choice_value-current_value+current_diff-choice_diff) <= 40:
            # max 20 point difference b/w column scores can be considered for Randomization procedure
            difference = choice_value - current_value
            sorted_id_list = sorted_id_list + [current_id]*int(5-(difference/4))  # more valuable column Id should be in
            # higher number than lower values i.e. lowering the chance of choosing lower yielding column by random.choice
        target_score_list[current_id] = "Done"
    # print(sorted_id_list)  # for debugging
    random.shuffle(sorted_id_list)  # shuffling the values for Randomization
    random.shuffle(sorted_id_list)  # shuffling the values for Randomization
    return random.choice(sorted_id_list)  # choosing a random value from sorted_id_list(abundance of higher scoring column is higher)


# function to take input from human player(s)
def man_turn(master_array, char):
    go = True
    while go:
        try:
            ask = int(input("\nEnter the column number ( for '"+char+"' ) : ")) - 1 # taking input from user
            # [-1 is used to adjust indexing anomaly]
            add(master_array, char, ask)  # appending player's char to chosen column in master_array
            point = get_fall_point(master_array, ask)
            print('\n' * (24 - row_count - 5))  # for spacing
            go = False
        except TypeError:  # function 'add' raises TypeError in case of filled column error
            print("\nThe given column is completely filled !")
        except IndexError:  # function 'add' raises IndexError in case of unavailable column error
            print("\nThe given column Does not exist !")
        except ValueError:  # in case of wrong or string input, int() raises ValueError
            print("\nPlease Enter a valid column value ! ")
    if has_won(master_array, (point[0] + 1, point[1]), char):  # Checking for if player has won the game
        print('\n' + char + ' has won the game !')
        print_box(master_array)
        return True


# function for computer turn
def comp_turn(master_array, char):
    print('\n' * (24 - row_count - 5))  # for spacing
    comp_choice = choose_column(master_array, char)  # choosing perfect column with choose_column() function
    add(master_array, char, comp_choice)   # appending computer's char to chosen column(comp_choice) in master_array
    point = get_fall_point(master_array, comp_choice)
    print("\ncomputer has chosen column number ", comp_choice + 1)  # print computer's choice [-1 is used to adjust indexing anomaly]
    if has_won(master_array, (point[0] + 1, point[1]), char):   # Checking for if player has won the game
        print('\n' + char + ' has won the game !')
        print_box(master_array)
        return True


# function to change player char(ID)
def change_player(char):
    if char == 'x':  # 'x' ===> '0'
        char = '0'
    else:  # '0' ===> 'x'
        char = 'x'
    return char


# ------------------------------------------------------calling the defined functions----------------------------------
print('''
-------------------------------------------------------------------------------
INSTRUCTION : Welcome to the game 'Connect Four';Here you will be able to drop 
your character (player ID) in the columns of game box by entering the number 
above the column.To win the match,player should be try to match his ID four(4) 
times in Horizontal, Vertical or Diagonal line before another player can do so.
--------------------------------------------------------------------------------
''')

Go = True
while Go:
    try:
        col_num = int(input("\nEnter the number of columns : "))  # taking column number input
        height = int(input("\nEnter the height: "))  # taking height input
        if col_num >= 15 or col_num <= 6 or height >= 15 or height <= 6:  # Checking for defined range [i.e. 6 < Height < 15 and 6 < Column < 15]
            raise ValueError("\nwrong input")
        else:
            Go = False
    except ValueError:  # violation of range or invalid input
        print("\nPlease enter valid values...[i.e. 6 < Height < 15 and 6 < Column < 15]")

master_array = np.array(list('.'*(col_num*height)))  # initial blank game array [ filled with '.' ]
master_array.shape = (height, col_num)  # adjusting the order of game array
row_count = height
column_count = col_num

play = input("\nPlay with computer ? [Y/N] : ")  # for man vs man OR man vs comp ?
if play == 'Y' or play == 'y':
    inp = input("\n['X' will have first turn ] => Enter x for taking 'X' or o for taking 'O': ")  # computer first OR
    if (inp == 'o' or inp == 'O') or inp == '0':                                                     # man first ?
        start = False  # for computer first case
    else:
        start = True  # for computer later case
else:
    start = True  # for no computer case

char = 'x'
if not start:  # for computer first case, start = False ==> not start = True
    win = comp_turn(master_array, char)  # for computer turn.win is useless here (winning is not possible in first turn)
    char = change_player(char)  # changing player ID

start_time = datetime.datetime.now()  # starting time counting
while '.' in master_array.flatten():  # True when full game box is not filled
    print_box(master_array)  # printing game box
    win = man_turn(master_array, char)  # calling man_turn for human player
    if win:  # case of winning of player ==> loop breaks
        break
    elif '.' not in master_array.flatten():  # full game box is filled ==> break
        continue
    char = change_player(char)  # changing player ID
    if play == 'Y' or play == 'y':  # man vs computer game ==> computer will play next
        win = comp_turn(master_array, char)  # calling comp_turn for computer player
        if win:  # case of winning of computer ==> loop breaks
            break
        char = change_player(char)  # changing player ID
else:
    print("\ngame is draw!")  # full game box is filled
    char = 'None'  # winner will be no one

# summary section :
print("\nSUMMARY : ")
print("\nTime taken : ", datetime.datetime.now()-start_time)  # printing total time passed
print('\nWinner is :'+" '"+char+"'")  # printing winner of game

nothing = input("\nEnter to exit : ")
