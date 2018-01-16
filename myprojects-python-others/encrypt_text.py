import string

def change_letter(letter,increment):
    l = list(string.printable[0:95]+string.letters[52:])+list(string.printable[0:95]+string.letters[52:])
    try:
        return l[l.index(letter)+increment]
    except:
        return letter
    
def recover_letter(letter,decrement):
    l = list(string.printable[0:95])+list(string.printable[0:95])
    try:
        return l[l.index(letter)-decrement]
    except:
        return letter


def get_increment(password):
    password = str(abs(hash(password)))
    while True:
        for i in password:
            yield int(i)
    

def encrept_word(word,password):
    gen = get_increment(password)
    s = ''
    for i in word:
        s += change_letter(i,gen.next())
    return s

def decrept_word(word,password):
    gen = get_increment(password)
    s = ''
    for i in word:
        s += recover_letter(i , gen.next())
    return s

inputfile = raw_input("[INPUT FILE] : Enter the infile name : ")
outputfile = raw_input("[OUTPUT FILE] : Enter the outfile name : ")
password = raw_input("[PASSWORD] : Enter the password : ")
mode = raw_input("[MODE] : Enter '1' for encryption or '0' for decryption : ")
try:
    fin = file(inputfile,'rb')
    fout = file(outputfile,'wb')
    text = 'anything'
    while text != '':
        text = fin.read(50000)
        if mode == '0':
            fout.write(decrept_word(text,password))
        elif mode == '1':
            fout.write(encrept_word(text,password))
        else:
            raise Exception("You must provide a proper mode !")
        print 'working ... '+str(fout.tell())
    fin.close()
    fout.close()
except Exception as error:
    print '[Error Occured] : '+str(error)


    
