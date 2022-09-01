from __future__ import division
import glob,os,time,string,re

count = 1
sucess = 0

def notdir(directory):
    try:
        os.chdir(directory)
        return False
    except:
        return True
    

def is_text(filename):
    s=open(filename).read(1024)
    text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
    _null_trans = string.maketrans("", "")
    if "\0" in s:
        return False
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    t = s.translate(_null_trans, text_characters)
    # If more than 50% non-text characters, then
    # this is considered a binary file
    if float(len(t))/float(len(s)) > 0.50:
        return False
    return True

def find_phrase(filepath,phrase):
    global count,sucess,regex
    try:
        if not is_text(filepath):
            raise Exception('binary file')
        f = file(filepath,'r')
        print "["+str(count)+"]"+" Scanning -->",filepath,"...",
        count += 1
        text = 'something'
        while text != '':
            text = f.read(50000000)
            if regex == 'Y' or regex == 'y':
                serchobj = re.search(phrase,text)
                if serchobj != None:
                    print "[SUCESS] >> Phrase found !"
                    sucess += 1
                    return True
                else:
                    print '.',
            else:
                if phrase in text:
                    print "[SUCESS] >> Phrase found !"
                    sucess += 1
                    return True
                else:
                    print '.',
        else:
            print "[FAILURE] >> Phrase not found !"
            return False
    except:
        print "["+str(count)+"]"+"Scipping binary file at..",filepath
        count += 1
        
def listmaker(dirt):
    fixed = []
    fixedir = []
    listdir = [dirt]
    
    print "\nScanning all contents in the directory......\n"
    while True:
        addir = []
        for dirname in listdir:
            subdir = glob.glob(dirname+'\\*')
            if (len(subdir) == 0) and notdir(dirname):
                fixed.append(dirname)
                check = find_phrase(dirname,phrase)
                if check:
                    sorted_list.append(dirname)
                    filename_file.writelines(dirname+'\n')
            else:
                addir = addir + subdir
                try:
                    os.chdir(dirname)
                    fixedir.append(dirname)
                except:
                    pass
        if len(addir) == 0:
            return fixed,fixedir
        else:
            listdir = list(addir)


    

dirinput = raw_input("Enter the directory path : ")
regex = raw_input("Use Regular Expression? (y/n) : ")
phrase = raw_input("Enter the search phrase : ")
check = raw_input("Search as a whole word (y/n) : ")
if check == 'y' or check == 'Y':
    phrase = " "+phrase+" "
filename_new = raw_input("Enter the a filepath to store the result : ")
if filename_new == '':
    filename_file = file('D:'+"\\sorted_dir_list.txt",'w')
    print "Using default storing filepath..."
else:
    filename_file = file(filename_new,'w')
sorted_list = []
try:
    os.chdir(dirinput)
    filelist,dirlist = listmaker(dirinput)
    for filedir in filelist:
        check = find_phrase(filedir,phrase)
        if check:
            sorted_list.append(filedir)
            filename_file.writelines(filedir+'\n')

    print "\nRESULT : \n"
    for f in sorted_list:
        print f
    
    print "\nTotal phrase containing file count :",sucess
    
except Exception as wrong:
    print "Unable to find the given directory...."
    print wrong
    time.sleep(5)
    exit()

filename_file.close()
x = raw_input("")

    
