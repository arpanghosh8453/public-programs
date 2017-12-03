#-----------------------------------------------import modules-------------------------------------------------------------
import random
import getpass
import datetime
#------------------------------------------------User Authentification-------------------------------------------------------


print "\n * Copyright \xa9 : Arpan Ghosh *\n"

#this part of code is for authentification ; removing this comment will ask for a password !
'''
print " * This game is created by Arpan Ghosh. \xae All rights reserved .\n"
print " * Verification : Enter the ",
password = getpass.getpass()
if hash(password) == -809589229:
    print "\nAcess granted : Welcome to the Dots & Boxes game !!\n"
else:
    print "\nError : Wrong password input...Sorry!\n"
    x = raw_input("Press Enter to exit!!")
    exit()
'''
print "\nINSTRUCTIONS :\n"
print "This game is based upon dots & boxes....By Entering the point ID (e.g. a0,a1,a2,b0,b1,b2......) Identify the points you want to join"
print "The computer will join the points! Now if you are playing with computer,the next chances will be carried out computer itself...."
print "Results will be decleared when the game is over ! Have fun with this game !"
print "\n >>> Game Starts......"

#----------------------------------------------Collecting Informations---------------------------------------------------------------------

prev_text = ""
n = int(raw_input("\nEnter the box length ( 2..9 ) : "))#getting the box length from user

while n < 2 or n > 9:
    print "Please enter a number between 2 and 9..."
    n = int(raw_input("Enter the box length ( 2..9 ) : "))

hor_links = [False] * (n * (n + 1))#Defining horizontal link connections(now all False)
ver_links = [False] * (n * (n + 1))#Defining vertical link connections(now all False)
owners = [' '] * (n ** 2)#defining the owners of created boxes(now blank)
alphabets = list('abcdefghijklmnopqrstuvwxyz')[0:(n + 1)]
numbers = list('0123456789')[0:(n + 1)]
dots = []#List for points ID
for num in numbers:
    for i in alphabets:
        dots.append(i + num)
#score definition
score1 = 0
score2 = 0
#selection of second Player
ask = raw_input("\nDo you want to play with computer? ( y / n ) :")
#Player name selection
if ask == 'y' or ask == 'Y':
    player1 = 'P'
    player2 = 'C'
else:
    player1 = '1'
    player2 = '2'

player = player1

#-------------------------------------------------Function definitions for duel play----------------------------------------------------

#function for checking if two points are joined or not
def is_linked(pos1, pos2, hor_links, ver_links):
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if (pos1 + 1) % (n + 1) == 0 and pos2 % (n + 1) == 0:
        return False
    if pos2 - pos1 == n + 1:
        return ver_links[pos1]
    elif pos2 - pos1 == 1:
        return hor_links[pos1 - ((pos1 + 1) // (n + 1))]
    else:
        return False

#part of the following printer function : Helps in same line printing
def part_print(new_text, end=""):
    global prev_text
    prev_text = prev_text + new_text
    if end == "\n":
        print prev_text
        prev_text = ""
    else:
        prev_text = prev_text + end

#Prints the dots and links and scores in a user friendly manner
def printer(hor_links, ver_links, owners):
    new_hor_links = []
    for i in hor_links:
        if i:
            new_hor_links.append('___')
        else:
            new_hor_links.append('   ')
    new_ver_links = []
    for i in ver_links:
        if i == True:
            new_ver_links.append('|   ')
        else:
            new_ver_links.append('    ')
    char = '#'
    hor_index = 0
    ver_index = 0
    owner_index = 0
    row_index = 0
    print '-' * (((n + 1) * 4) + 8) + '\n'
    print "    a   b   c   d   e   f   g   h   i   j   "[0:((n + 1) * 4) + 1] + '\n'
    while True:
        print " " + str(row_index) + ' ',
        for i in range(n):
            part_print(char, "")
            part_print(new_hor_links[hor_index], "")
            hor_index += 1
        part_print(char, "\n")
        row_index += 1
        if (hor_index) == len(new_hor_links):
            break
        print "   ",
        for i in range(n + 1):
            part_print(new_ver_links[ver_index], "")
            ver_index += 1
        part_print("", "\n")
        ver_index -= (n + 1)
        print "   ",
        for i in range(n):
            if ver_links[ver_index]:
                part_print("| " + owners[owner_index] + " ", "")
            else:
                part_print("  " + owners[owner_index] + " ", "")
            owner_index += 1
            ver_index += 1
        if ver_links[ver_index]:
            part_print("|", "\n")
        else:
            part_print(" ", "\n")
        ver_index += 1
    print '\n\n' + '-' * (((n + 1) * 4) + 8)
    print "\nscore of player one (", player1, ") : " + str(score1)
    print "score of player two (", player2, ") : " + str(score2)

#Checks if the given four points are joined correctly so that a box is formed
def is_box_completed(pos1, pos2, pos3, pos4, hor_links, ver_links):
    all = [pos1, pos2, pos3, pos4]
    all.sort()
    for i in all:
        if i < 0 or i > (((n + 1) ** 2) - 1):
            return False
    if (is_linked(all[0], all[1], hor_links, ver_links) and is_linked(all[2], all[3], hor_links, ver_links)) and (
                is_linked(all[0], all[2], hor_links, ver_links) and is_linked(all[1], all[3], hor_links, ver_links)):
        return True
    else:
        return False

#checks if the given points are joined and returns a list of topmost left points of the box created .
# if no box is formed, returns [].
#raises error if the points cannot be joined !
def create_link(pos1, pos2, hor_links, ver_links):
    e = Exception("Error")
    if is_linked(pos1, pos2, hor_links, ver_links):
        raise RuntimeError("already present")
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if (pos1 + 1) % (n + 1) == 0 and pos2 % (n + 1) == 0:
        raise e
    if pos2 - pos1 == n + 1:
        ver_links[pos1] = True
        box_id = []
        check = is_box_completed(pos1, pos2, pos1 - 1, pos2 - 1, hor_links, ver_links)
        if check:
            box_id.append(pos1 - 1)
        check = is_box_completed(pos1, pos2, pos1 + 1, pos2 + 1, hor_links, ver_links)
        if check:
            box_id.append(pos1)
        return box_id
    elif pos2 - pos1 == 1:
        hor_links[pos1 - ((pos1 + 1) // (n + 1))] = True
        box_id = []
        check = is_box_completed(pos1, pos2, pos1 - (n + 1), pos2 - (n + 1), hor_links, ver_links)
        if check:
            box_id.append(pos1 - (n + 1))
        check = is_box_completed(pos1, pos2, pos1 + (n + 1), pos2 + (n + 1), hor_links, ver_links)
        if check:
            box_id.append(pos1)
        return box_id
    else:
        raise e

#removes a link from the given points by making the joining index False in the hor_links or ver_links
#does nothing if the link is absent
def remove_link(pos1, pos2, hor_links, ver_links):
    e = Exception("Error")
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if (pos1 + 1) % (n + 1) == 0 and pos2 % (n + 1) == 0:
        raise e
    if (pos2 - pos1) == n + 1:
        ver_links[pos1] = False
    elif (pos2 - pos1) == 1:
        hor_links[pos1 - ((pos1 + 1) // (n + 1))] = False
    else:
        raise e

#receives the corner(left topmost point of the box) value and changes its ownership to player name
def change_owner(corner, owners, player):
    if corner != []:
        owners[corner - ((corner + 1) // (n + 1))] = player
        return True
    else:
        return False

#reverses the current player
def change_player():
    global player
    if player == player1:
        player = player2
    else:
        player = player1

#---------------------------------------------------Function definition for Computer player----------------------------------------

#joins every links and checks if a box is created, if not : Deletes the link , else: Keeps it
def comp_complete_box(virtual_hor_links, virtual_ver_links):
    link_joined = []
    box_count = 0
    for i in range((n + 1) ** 2):
        try:
            flag = create_link(i, i + 1, virtual_hor_links, virtual_ver_links)
            if flag == []:
                remove_link(i, i + 1, virtual_hor_links, virtual_ver_links)
            else:
                link_joined.append((i, i + 1))
            box_count += len(flag)
        except:
            pass
        try:
            flag = create_link(i, i + n + 1, virtual_hor_links, virtual_ver_links)
            if flag == []:
                remove_link(i, i + n + 1, virtual_hor_links, virtual_ver_links)
            else:
                link_joined.append((i, i + n + 1))
            box_count += len(flag)
        except:
            pass
    return link_joined, box_count, virtual_hor_links, virtual_ver_links

#calls the comp_complete_box untill the is a slightest chance of gaining a box
def comp_try_box(hor_links, ver_links):
    virtual_hor_links = list(hor_links)
    virtual_ver_links = list(ver_links)
    link_joined = []
    box_count = 0
    while True:
        prev_length = box_count
        new_links, count, virtual_hor_links, virtual_ver_links = comp_complete_box(virtual_hor_links, virtual_ver_links)
        link_joined = link_joined + new_links
        box_count += count
        if box_count == prev_length:
            break
    return link_joined, box_count, virtual_hor_links, virtual_ver_links

#final Turns generater!
#comes into play when all chances of gaining a box is gone!
#joins all not joined lines one by one and counts the posibility of gaining a box by the oppernent, then remove the joining
#the least box gaining possibility is selected
#takes a random chance from the least possibilities and appends to the link_joined list ,hence generates the final turn chances
def get_comp_turns(link_joined, virtual_hor_links, virtual_ver_links):
    if (False not in virtual_hor_links) and (False not in virtual_ver_links):
        least_gainable_box_count = 0
    else:
        least_gainable_box_count = (n + 1) ** 2
    link_available = []
    count = 0
    for link in virtual_hor_links:
        if link == False:
            virtual_hor_links[count] = True
            new_link, new_count, H, V = comp_try_box(virtual_hor_links, virtual_ver_links)
            for link in new_link:
                remove_link(link[0], link[1], virtual_hor_links, virtual_ver_links)
            if new_count < least_gainable_box_count:
                least_gainable_box_count = new_count
                link_available = []
                link_available.append(((count // n) + count, (count // n) + (count + 1)))
            elif new_count == least_gainable_box_count:
                link_available.append(((count // n) + count, (count // n) + (count + 1)))
            virtual_hor_links[count] = False
        count += 1
    count = 0
    for link in virtual_ver_links:
        if link == False:
            virtual_ver_links[count] = True
            new_link, new_count, H, V = comp_try_box(virtual_hor_links, virtual_ver_links)
            for link in new_link:
                remove_link(link[0], link[1], virtual_hor_links, virtual_ver_links)
            if new_count < least_gainable_box_count:
                least_gainable_box_count = new_count
                link_available = []
                link_available.append((count, count + n + 1))
            elif new_count == least_gainable_box_count:
                link_available.append((count, count + n + 1))
            virtual_ver_links[count] = False
        count += 1

    if len(link_joined) >= 3 and least_gainable_box_count >= 2:#a special winning trick is special cases only!
        del link_joined[-2]
        return link_joined
    else:
        if link_available != []:
            link_joined.append(random.choice(link_available))#general case
        return link_joined

#calls the comp_try_box and get_comp_turns one by one and joins the links(returned from get_comp_turns) and changes the ownership!
def comp_play(hor_links, ver_links):
    print "\nTurn for computer..."
    global owners, score2, dots
    box_link_list, box_count, new_hor_links, new_ver_links = comp_try_box(hor_links, ver_links)
    turn_list = get_comp_turns(box_link_list, new_hor_links, new_ver_links)
    for turn in turn_list:
        box_id = create_link(turn[0], turn[1], hor_links, ver_links)
        flag = False
        for corner in box_id:
            flag = change_owner(corner, owners, "C")
            if flag:
                print "\nComputer owns a score!"
                score2 += len(box_id)
        print "\nline created between", dots[turn[0]], "and", dots[turn[1]],'\n'
        if flag == False:
            break
        else:
            printer(hor_links, ver_links, owners)
    print "\ncomputer has completed its chance(s)!"

#-------------------------------------------------------Final game structure---------------------------------------------------

def start_game():

    global score1, score2
    start_time = datetime.datetime.now()
    while ' ' in owners:#Loop for game coninution
        print '\n'
        printer(hor_links, ver_links, owners)#prints the boxes
        print "\n"
        ok = 0
        #Point input from user
        point1 = raw_input("Enter the first point for " + player + " : ")
        point2 = raw_input("Enter the second point for " + player + " : ")
        try:
            if point1[-1] == '\r' and point2[-1] == '\r':
                point1 = point1[0:len(point1) - 1]
                point2 = point2[0:len(point2) - 1]
        except:
            pass
        dont_change = False#checks if the the player cotinues the game or the turn will be shifted to another
        while ok == 0:
            dont_change = False
            try:
                pos1 = dots.index(point1)
                pos2 = dots.index(point2)
                box_id = create_link(pos1, pos2, hor_links, ver_links)
                for corner in box_id:
                    dont_change = change_owner(corner, owners, player)#Dont_change changes if box is created
                print "\nline created between " + point1 + " and " + point2
                ok = 1
            #Checks Errors for wrong point input
            except RuntimeError:
                print "\nThe given points are already joined!\n"
                point1 = raw_input("Enter the first point for " + player + " : ")
                point2 = raw_input("Enter the second point for " + player + " : ")
            except ValueError:
                print "\nThe given points are not found!\n"
                point1 = raw_input("Enter the first point for " + player + " : ")
                point2 = raw_input("Enter the second point for " + player + " : ")
            except:
                print "\nThe given points cannot be joined!\n"
                point1 = raw_input("Enter the first point for " + player + " : ")
                point2 = raw_input("Enter the second point for " + player + " : ")

        if dont_change:#if true the current player will continue the game
            if player == 'P' or player == '1':
                score1 += len(box_id)
            else:
                score2 += len(box_id)
            print "\nPlayer " + player + " owns a point!"
            if " " not in owners:
                break
        else:
            if player2 == 'C':#checks if computer will play
                comp_play(hor_links, ver_links)
            else:
                change_player()#changes the player

    #Actions after game is over
    print "\nGame over!!\n"
    printer(hor_links, ver_links, owners)
    diff = score1 - score2
    #prints the score difference and the owners name
    if diff < 0:
        print "\nPlayer 2" + "(" + player2 + ")" + " has won the match with " + str(abs(diff)) + " points"
    elif diff > 0:
        print "\nPlayer 1" + "(" + player1 + ")" + " has won the match with " + str(abs(diff)) + " points"
    else:
        print "\nThe game is draw!"
    end_time = datetime.datetime.now()
    print "\nTotal Playing Time :",
    print (end_time - start_time)
    exit = raw_input("\nPress Enter to exit : ")#Pauses the script

start_game()#initiates the game