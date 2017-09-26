print "Welcome to the word-game !!\nIn this game you will be asked to enter a word and then computer will give you a word with the last letter of your word . Nextly,You will be asked to enter a word with the last letter given by the computer . If you are unable to give such a word anytime, pleaseenter '~' to continue the game by the computer itself !!\n\nLet's start..."
print '-'*50

import random
word_num = 1

Afile = open("/home/arpan/Desktop/dictionary/Aword.csv", 'r')
Bfile = open("/home/arpan/Desktop/dictionary/Bword.csv", 'r')
Cfile = open("/home/arpan/Desktop/dictionary/Cword.csv", 'r')
Dfile = open("/home/arpan/Desktop/dictionary/Dword.csv", 'r')
Efile = open("/home/arpan/Desktop/dictionary/Eword.csv", 'r')
Ffile = open("/home/arpan/Desktop/dictionary/Fword.csv", 'r')
Gfile = open("/home/arpan/Desktop/dictionary/Gword.csv", 'r')
Hfile = open("/home/arpan/Desktop/dictionary/Hword.csv", 'r')
Ifile = open("/home/arpan/Desktop/dictionary/Iword.csv", 'r')
Jfile = open("/home/arpan/Desktop/dictionary/Jword.csv", 'r')
Kfile = open("/home/arpan/Desktop/dictionary/Kword.csv", 'r')
Lfile = open("/home/arpan/Desktop/dictionary/Lword.csv", 'r')
Mfile = open("/home/arpan/Desktop/dictionary/Mword.csv", 'r')
Nfile = open("/home/arpan/Desktop/dictionary/Nword.csv", 'r')
Ofile = open("/home/arpan/Desktop/dictionary/Oword.csv", 'r')
Pfile = open("/home/arpan/Desktop/dictionary/Pword.csv", 'r')
Qfile = open("/home/arpan/Desktop/dictionary/Qword.csv", 'r')
Rfile = open("/home/arpan/Desktop/dictionary/Rword.csv", 'r')
Sfile = open("/home/arpan/Desktop/dictionary/Sword.csv", 'r')
Tfile = open("/home/arpan/Desktop/dictionary/Tword.csv", 'r')
Ufile = open("/home/arpan/Desktop/dictionary/Uword.csv", 'r')
Vfile = open("/home/arpan/Desktop/dictionary/Vword.csv", 'r')
Wfile = open("/home/arpan/Desktop/dictionary/Wword.csv", 'r')
Xfile = open("/home/arpan/Desktop/dictionary/Xword.csv", 'r')
Yfile = open("/home/arpan/Desktop/dictionary/Yword.csv", 'r')
Zfile = open("/home/arpan/Desktop/dictionary/Zword.csv", 'r')


def list_changer(your_list):
    lines = your_list.readlines()
    returnlist = []
    for i in range(len(lines)):
        text = lines[i].strip()
        returnlist .append(text)
    return returnlist

    
Alist = list_changer(Afile)
Blist = list_changer(Bfile)
Clist = list_changer(Cfile)
Dlist = list_changer(Dfile)
Elist = list_changer(Efile)
Flist = list_changer(Ffile)
Glist = list_changer(Gfile)
Hlist = list_changer(Hfile)
Ilist = list_changer(Ifile)
Jlist = list_changer(Jfile)
Klist = list_changer(Kfile)
Llist = list_changer(Lfile)
Mlist = list_changer(Mfile)
Nlist = list_changer(Nfile)
Olist = list_changer(Ofile)
Plist = list_changer(Pfile)
Qlist = list_changer(Qfile)
Rlist = list_changer(Rfile)
Slist = list_changer(Sfile)
Tlist = list_changer(Tfile)
Ulist = list_changer(Ufile)
Vlist = list_changer(Vfile)
Wlist = list_changer(Wfile)
Xlist = list_changer(Xfile)
Ylist = list_changer(Yfile)
Zlist = list_changer(Zfile)


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

while True:
    
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
            
            
        
        
    
    
