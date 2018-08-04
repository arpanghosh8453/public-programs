import re, datetime, getpass
#-----------------------------------Authenthification----------------------------
print "\n** Copyright : Arpan Ghosh ** \n"
print "This Programme is Programmed by Arpan Ghosh. All rights reserved .\n"
print "Verification : Enter the ",
password = getpass.getpass()
if hash(password) == -809589229:#MATCHING HASH PASSWORD VALUE
    print "\nAccess granted : Welcome to the word conversion programme!\n"
else:
    print "\nError : Wrong password input...Sorry!\n"
    x = raw_input("Press Enter to exit!!")
    exit()
print '\n'+'-'*80
#------------------------------Functions---------------------------------------------------

#generates every possible dictionary words by replacing a single letter
#and returns a dictionary of list of values with a index of the changed letter and placeof the letter


def replace_letter(word,name,wordlist):
    dictionary = {}
    pos = 1
    for letter in word:
        extension = str(pos)+letter
        changed = list(word)
        changed[pos-1] = '.'
        template = ''.join(changed)
        words = re.findall('\n'+template+'\n','\n'+'\n\n'.join(wordlist)+'\n')
        result = []
        for w in words:
            result.append(w[1:len(w)-1])
        dictionary[name+extension] = result
        pos += 1
    return dictionary

#tekes a dictionary(for recursion of the generated dict from replace_letter func)
#calls the replace_letter for every value of every index
#returns a bigger dict of next layer combination


def expand_dict(dictionary,wordlist):
    indexes = dictionary.keys()
    result = {}
    for index in indexes:
        words = dictionary[index]
        for word in words:
            new_dict = replace_letter(word,index,wordlist)
            for key in new_dict:
                if key in result.keys():
                    result[key] = result[key]+new_dict[key]
                else:
                    result[key] = new_dict[key]
    return result

#remove the previous layer's word from the main wordlist


def remove_words(dictionary,wordlist):
    value_list = dictionary.values()
    for vlist in value_list:
        for value in vlist:
            try:
                wordlist.remove(value)
            except:
                pass
    return wordlist

#interpretes the index code to transformation of words


def print_func(target_word,index,save):
    print ''
    pos = ''
    list_index = []
    index = index.lstrip()
    for i in index:
        if i in '1234567890':
            pos += i
        else:
            list_index.append((i,int(pos)-1))
            pos = ''
    word = list(target_word)
    list_word = [target_word]
    for item in list_index[::-1]:
        word[item[1]] = item[0]
        list_word.append(''.join(word))
    string = ' --> '.join(list_word[::-1])
    print string
    if save:
        outfile.write(string+"\n\n")
                

start_word = raw_input("Enter the starting word : ")
target_word = raw_input("Enter the ending word : ")
repeat = int(raw_input("Enter the layer number to be generated : "))
filename = raw_input("Enter the file adress to store the result : ")

then = datetime.datetime.now()

if len(start_word) != len(target_word) : raise Exception("Lengths of the words should not differ!")

#Checking for dictionary availability
try:
    f = file("C:\\Users\\libr\\programs\\dict.txt",'r')
except:
    print "default dictionary location is unavilable"
    location = raw_input("Please enter a dictionary file location :")
    f = file(location,'r')
    
#Checking for storage file availability
if filename == '':
    save = False
else:
    try:
        outfile = file(filename,'a')
        outfile.write("\n\n"+"-"*90+"\n\n")
        outfile.write("Word Conversion : "+start_word+" --> "+target_word+"\n\n")
        save = True
    except:
        print "The given file adesss can't be created !"
        save = False

data = f.read()
allwordlist = data.split('\n')#list of all words of the dict file with newline
wordlist = []
#seperates the same length words
for word in allwordlist:
    if len(word) == len(start_word):
        wordlist.append(word)
    else:
        pass

if (start_word not in wordlist) or (target_word not in wordlist):raise Exception("Given word(s) not found in dictionary!")
wordlist.remove(start_word)
total_words_count = len(wordlist)

init_dict = {' ':[start_word]}
stop = False

print "\nProgress [Remaining words] : ",
for i in range(repeat):
    new_dict = expand_dict(init_dict,wordlist)
    indexes = new_dict.keys()
    for index in indexes:
        words = new_dict[index]
        if target_word in words:#checking for matching of target word
            if not stop:
                print ''
            print_func(target_word,index,save)
            stop = True#breaks the program after checking current layer
            
    if stop:
        break
    wordlist = remove_words(new_dict,wordlist)#removing words already occured  in current dict
    init_dict = new_dict
    print len(wordlist),#remaining words printing

if save:
    outfile.close()
now = datetime.datetime.now()
print "\nTime taken : ",now-then

x = raw_input("\nEnter to Exit : ")


