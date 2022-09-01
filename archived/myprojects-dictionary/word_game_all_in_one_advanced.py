print "Welcome to the word-game !!\nIn this game you will be asked to enter a word and then computer will give you a word with the last letter of your word . Nextly,You will be asked to enter a word with the last letter given by the computer . If you are unable to give such a word anytime, pleaseenter '~' to continue the game by the computer itself !!\n\nLet's start..."
print '-'*50

import random
word_num = 1

def list_changer(your_list):
    lines = your_list.readlines()
    returnlist = []
    for i in range(len(lines)):
        text = lines[i].strip()
        returnlist .append(text)
    return returnlist

def check_letter(word):
    for letter in word:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            pass
        else:
            return False
    return True
    


all_file = open("C:\\Users\\ACER\\Desktop\\dictionary\\all_in_one.csv", 'r')
all_list = list_changer(all_file)

Alist = []
Blist = []
Clist = []
Dlist = []
Elist = []
Flist = []
Glist = []
Hlist = []
Ilist = []
Jlist = []
Klist = []
Llist = []
Mlist = []
Nlist = []
Olist = []
Plist = []
Qlist = []
Rlist = []
Slist = []
Tlist = []
Ulist = []
Vlist = []
Wlist = []
Xlist = []
Ylist = []
Zlist = []

for word in all_list:
    try:
        if word[0] == 'a'and check_letter(word):
            Alist.append(word)
        elif word[0] == 'b'and check_letter(word):
            Blist.append(word)
        elif word[0] == 'c'and check_letter(word):
            Clist.append(word)
        elif word[0] == 'd'and check_letter(word):
            Dlist.append(word)   
        elif word[0] == 'e'and check_letter(word):
            Elist.append(word)
        elif word[0] == 'f'and check_letter(word):
            Flist.append(word)
        elif word[0] == 'g'and check_letter(word):
            Glist.append(word)
        elif word[0] == 'h'and check_letter(word):
            Hlist.append(word)
        elif word[0] == 'i'and check_letter(word):
            Ilist.append(word)
        elif word[0] == 'j'and check_letter(word):
            Jlist.append(word)
        elif word[0] == 'k'and check_letter(word):
            Klist.append(word)
        elif word[0] == 'l'and check_letter(word):
            Llist.append(word)   
        elif word[0] == 'm'and check_letter(word):
            Mlist.append(word)
        elif word[0] == 'n'and check_letter(word):
            Nlist.append(word)
        elif word[0] == 'o'and check_letter(word):
            Olist.append(word)
        elif word[0] == 'p'and check_letter(word):
            Plist.append(word)
        elif word[0] == 'q'and check_letter(word):
            Qlist.append(word)
        elif word[0] == 'r'and check_letter(word):
            Rlist.append(word)
        elif word[0] == 's'and check_letter(word):
            Slist.append(word)
        elif word[0] == 't'and check_letter(word):
            Tlist.append(word)
        elif word[0] == 'u'and check_letter(word):
            Ulist.append(word)
        elif word[0] == 'v'and check_letter(word):
            Vlist.append(word)   
        elif word[0] == 'w'and check_letter(word):
            Wlist.append(word)
        elif word[0] == 'x'and check_letter(word):
            Xlist.append(word)
        elif word[0] == 'y'and check_letter(word):
            Ylist.append(word)
        elif word[0] == 'z'and check_letter(word):
            Zlist.append(word)
        else:
            pass
    except Exception as error:
        print error

masterlist = [Alist,Blist,Clist,Dlist,Elist,Flist,Glist,Hlist,Ilist,Jlist,Klist,Llist,Mlist,Nlist,Olist,Plist,Qlist,Rlist,Slist,Tlist,Ulist,Vlist,Wlist,Xlist,Ylist,Zlist]
indexlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
used = []


def Check_word(word,last_letter,used):
    if word == '~':
        return '~'
    index = indexlist.index(last_letter)
    word_list = masterlist[index]
    if word in word_list:
        if word in used:
            return 'used'
        else:
            return 'ok'
    else:
        return 'wrong'

def Check_whole(word):
    for word_list in masterlist:
        if word in word_list:
            return True
    else:
        return False
def take_input(start):
    if start != "":
        start = "that starts with '"+start+"'"
    your_word = raw_input("["+str(word_num)+"] Please Enter a meaningful word"+start+" : ")
    your_word = your_word.lower()
    if your_word == '~' and len(used) != 0:
        return '~'
    while (not Check_whole(your_word) or (len(your_word)==1 and your_word != 'i'))or your_word[-1] not in 'abcdefghijklmnopqrstuvwxyz':
        if len(your_word)==1:
            print "Sorry : Word must not be single lettered"
        else:
            print "Sorry : Word is Incorrect !! "
        your_word = raw_input("["+str(word_num)+"] Please Enter a meaningful word"+start+" : ")
        if your_word == '~' and len(used) != 0:
            return '~'
        your_word = your_word.lower()
    return your_word

your_word = take_input("")
your_word = your_word.lower()
used.append(your_word)
word_num += 1

for i in range(100000):
    
        last_letter = your_word[-1]
        index = indexlist.index(last_letter)
        comp_word = random.choice(masterlist[index])
        while comp_word in used or (len(comp_word) == 1 or comp_word[-1] not in 'abcdefghijklmnopqrstuvwxyz'):
            comp_word = random.choice(masterlist[index])
        print "["+str(word_num)+"]Computer : My word is "+comp_word
        used.append(comp_word)
        word_num += 1
        your_word = take_input(comp_word[-1])
        if your_word == '~':
            print "Computer : I have won the match !! "
            your_word = comp_word
            continue
        reply = Check_word(your_word,comp_word[-1],used)
        while True:
            if reply == 'used':
                print "Sorry : The word is already used in word number "+str(used.index(your_word)+1)+" !!"
                your_word = take_input(comp_word[-1])
                reply = Check_word(your_word,comp_word[-1],used)
            elif reply == 'wrong':
                print "Sorry : Word is not perfectly started!!"
                your_word = take_input(comp_word[-1])
                reply = Check_word(your_word,comp_word[-1],used)
            elif reply == '~':
                print "Computer : I have won the match !! "
                your_word = comp_word
                break
            else:
                print random.choice(['good','well done','Excellent','nice','Great','Very Good'])
                break
        
        used.append(your_word)
        word_num += 1
else:
    print "I have lost the game !! "
    exit()
            
        
        
    
    
