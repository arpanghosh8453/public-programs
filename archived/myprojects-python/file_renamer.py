import os,glob,random
try:
    os.mkdir("C:\\rename")
except:
    pass
filename = file("C:\\rename\\list.csv","w")

def rand_name(length):
    name = ''
    for i in range(length):
        name = name+random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'))
    return name+".abc"
def not_dir(directory):
    try:
        os.chdir(directory)
        return False
    except:
        return True

def file_finder(directory):
    alldir = [directory]
    maindir = [directory]
    subdir = []
    filelist = []
    while True:
        for dirc in maindir:
            content = glob.glob(dirc+"\\*")
            for i in content:
                if not not_dir(i):
                    subdir.append(i)
                else:
                    filelist.append(i)
        if len(subdir) == 0:
            break
        maindir = list(subdir)
        alldir = alldir + subdir
        subdir = []
    return filelist


def rename(oldname):
    #print oldname
    broken = oldname.split("\\")
    broken.pop()
    broken.append(rand_name(7))
    #print broken
    newname = "\\".join(broken)
    #print newname
    try:
        os.rename(oldname,newname)
        print "SUCCESS :",oldname,"by",newname
        filename.write(oldname+","+newname+"\n")
    except Exception as error:
        print "FAILURE :",str(error)

        
def main(dirlist):
    for directory in dirlist:
        for name in file_finder(directory):
            #print name
            rename(name)

main(["E:\\test"])
filename.close()

