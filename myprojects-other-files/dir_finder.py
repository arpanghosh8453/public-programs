import glob,os,time

def notdir(dirname):
    try:
        os.chdir(dirname)
        return False
    except:
        return True

def listmaker(dirname,filehandle,dirhandle):
    listdir = [dirname]
    dircount = 0
    filecount = 0
    while True:
        addir = []
        for list_dirname in listdir:
            subdir = glob.glob(list_dirname+"\\*")
            if len(subdir) == 0 and notdir(list_dirname):
                filecount += 1
                filehandle.write("["+str(filecount)+"]"+" "+list_dirname+'\n')
            else:
                addir = addir + subdir
                dircount += 1
                dirhandle.write("["+str(dircount)+"]"+" "+list_dirname+'\n')
                print "["+str(dircount)+"]"+" "+list_dirname
        if len(addir) == 0:
            break
        else:
            listdir = list(addir)

dirinput = raw_input("Enter the directory path : ")
ask = raw_input("choose default destination files ??['D:\\file_list_store.txt' and 'D:\\directory_list_store.txt'] (y/n) : ")
if ask == 'y':
    filepath = 'D:\\file_list_store.txt'
    dirpath = 'D:\\directory_list_store.txt'
else:
    filepath = raw_input("Enter the directory path to save the file list: ")
    dirpath = raw_input("Enter the directory path to save the directory list: ")
try:
    os.chdir(dirinput)
    filehandle = file(filepath,'w')
    dirhandle = file(dirpath,'w')
except Exception as error:
    print "unable to access to the given Directory!!SORRY!!"
    print 'Cause of Error :',error
    time.sleep(5)
    exit()

listmaker(dirinput,filehandle,dirhandle)

filehandle.close()
dirhandle.close()








                
