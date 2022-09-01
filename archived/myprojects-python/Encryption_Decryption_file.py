#---------------------------------Imports---------------------------------------
from Crypto.Cipher import AES,DES
from Crypto import Random
import hashlib,os,sys,getpass,glob,random,math
#----------------------------------Authentification----------------------------------------
print "\n** Copyright : Arpan Ghosh ** \n"
print "This Programme is Programmed by Arpan Ghosh. All rights reserved .\n"
print "Verification : Enter the ",
password = getpass.getpass()
if hash(password) == -809589229:#MATCHING HASH PASSWORD VALUE
    print "\nAccess granted : Welcome to the Encryptor!\n"
else:
    print "\nError : Wrong password input...Sorry!\n"
    x = raw_input("Press Enter to exit!!")
    exit()
print '\n'+'-'*80
#-------------------------------------------------------------------------------------------
#non functional part
'''
def Create_directory(dirpath):
    if os.isdir(dirpath):
        ask = raw_input("\nDefault name "+dirpath+" already exists : Enter a proper directory name to avoid overwritting : ")
        if ask == '':
            os.rmdir(dirpath)
            os.mkdir(dirpath)
        else:
            os.mkdir(os.path.split(dirpath)[0]+'\\'+ask)
'''
#-----------------------Function for Progess bar generation---------------------------------

def calculate_progress(total_size,read_size):
    if total_size == 0:
        return None
    remaining = total_size-read_size
    time_const = 0.2/(1024*1024)
    time_rem = int(math.ceil(remaining*time_const))
    size_percent = int(math.ceil((read_size/float(total_size))*50))
    percent = size_percent * 2
    printable = "["+'#'*size_percent+' '*(50-size_percent)+'] '+str(percent)+'% '+"[Time:"+str(time_rem)+" second(s)]"
    print printable,
    print '\b'*(len(printable)+3),
    
#--------------------Function for getting only files sorted from dir--------------------------
    
def get_files(folder):
    all_list = glob.glob(folder+"\\*")
    file_list = []
    for item in all_list:
        if os.path.isfile(item):
            file_list.append(item)
        else:
            pass
    return file_list
            
#------------------Generarte random file name for file replacing with existing name------------

def rand_name(length):
    name = ''
    for i in range(length):
        name = name+random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'))
    return name+".tmp"

#-----------------main defination used for encryption----------------------------------------------
def Encrypt_file(password,mode,infile,outfile = None,overwrite = False,bytelen = 1024*1024):
    
    hash_value = hashlib.md5()
    hash_value.update(password)#getting a hash value for password
    
    if mode == '1':#for AES Encryption
        key = hash_value.digest()
        iv = Random.new().read(AES.block_size)#generating the random initialization vector for encryption
        cipher = AES.new(key, AES.MODE_CFB, iv)#getting the cipher method
    else:#for DES encryption
        key = hash_value.digest()[0:8]#resizing the hash value to 8 byte
        iv = Random.new().read(DES.block_size)
        cipher = DES.new(key, DES.MODE_CFB, iv)#getting the cipher method

    #Finding a output file if not given
    if not outfile:
        outfile = infile+'.enc'
    check = os.path.exists(outfile)
    if check == True and overwrite == False:
        path = raw_input("\nDefault name "+outfile+" already exists : Enter a proper file name to avoid overwritting : ")
        if path:
            outfile = os.path.dirname(infile)+'\\'+path
        
    outfile = file(outfile,'wb')
    outfile.write(iv)
    
    with open(infile,'rb') as f:
        if os.path.getsize(infile) == 0:#Escape root for 0 byte file
            print "Blank file found.....Aborting...."
            return None
        print "\nEncrypting file :",infile,"to",outfile.name,"[",os.path.getsize(infile),"Bytes ]\n\n",
        print "\n Status : \n"
        while True:
            chunk = f.read(bytelen)
            calculate_progress(os.path.getsize(infile),f.tell())#showing the progress bar(w.r.t. bytelen = 1024*1024)
            if chunk == '':
                break
            else:
                pass
            encrypted_data = cipher.encrypt(chunk)#Encrypting the chunk with Cipher method
            outfile.write(encrypted_data)#writting it to output file
            
    outfile.close()
    print "\n\nEncryption Successful :",infile,"to",outfile.name
    if overwrite:
        os.remove(infile)
        os.rename(outfile.name,infile)
        print "\nSucessfully overwritten on",infile
    print '-'*80
    
#-----------------main defination used for Decryption----------------------------------------------
    
def Decrypt_file(password,mode,infile,outfile = None,overwrite = False,bytelen = 1024*1024):
    #same methods are followed as encryption
    hash_value = hashlib.md5()
    hash_value.update(password)
    
    if not outfile:
        if infile.endswith('.enc'):
            outfile = os.path.splitext(infile)[0]
        else:
            outfile = infile+'.dec'
            
    check = os.path.exists(outfile)
    if check == True and overwrite == False:
        path = raw_input("\nDefault name "+outfile+" already exists : Enter a proper file name to avoid overwritting : ")
        if path:
            outfile = os.path.dirname(infile)+'\\'+path
        
    outfile = file(outfile,'wb')
    if os.path.getsize(infile) == 0:
        print "Blank file found.....Aborting...."
        return None
    with open(infile,'rb') as f:
        
        print "\nDecrypting file :",infile,"to",outfile.name,"[",os.path.getsize(infile),"Bytes ]\n\n",
        
        if mode == '1':
            iv = f.read(16)#getting the initialization vector for decryption(16 byte)
            key = hash_value.digest()
            cipher = AES.new(key, AES.MODE_CFB, iv)
        else:
            iv = f.read(8)#getting the initialization vector for decryption(8 byte)
            key = hash_value.digest()[0:8]
            cipher = DES.new(key, DES.MODE_CFB, iv)
        print "\n Status : \n"
        while True:
            chunk =  f.read(bytelen)
            calculate_progress(os.path.getsize(infile),f.tell())#(w.r.t. bytelen = 1024*1024)
            if chunk == '':
                break
            else:
                pass
            decrypted_data = cipher.decrypt(chunk)#Decrypting the chunk with Cipher method
            outfile.write(decrypted_data)
            
    outfile.close()
    print "\n\nDecryption Successful :",infile,"to",outfile.name
    if overwrite:
        os.remove(infile)
        os.rename(outfile.name,infile)
        print "\nSucessfully overwritten on",infile
    print '-'*80

#----------------------------------------Method for whole directory encryption(file by file)-------------------------------
def Dir_Encrypt_Decrypt(dirname,choice,mode,password,code,level,overwrite):
    listdir = [dirname]
    dircount = 0
    filecount = 0
    if level == True:#for sub-directory encryption
        while True:
            addir = []
            for list_dirname in listdir:
                subdir = glob.glob(list_dirname+"\\*")
                if len(subdir) == 0 and not os.path.isdir(list_dirname):
                    if choice == 'y' or choice == 'Y':#for Turn on run time file selection
                        ask = raw_input("\nEncrypt this file : "+list_dirname+' (y/n) ==> ')
                    else:
                        ask = 'y'
                    if ask != 'y' and ask != 'Y':
                        print "\nOk....This file is skipped ...!"
                        print '-'*80
                    else:
                        filecount += 1
                        if code == '1':#for Encryption
                            ask_try = 'y'
                            while ask_try == 'y' or ask_try == 'Y':
                                try:
                                    Encrypt_file(password,mode,list_dirname,'',overwrite)#calling the Encrypt_file function with parameters
                                    ask_try = 'n'
                                except Exception as error:
                                    print "\nError Occured when Encrypting file :",list_dirname
                                    print error
                                    ask_try = raw_input("\nTry Again (y/n) : ")#if failed due to any reason, it can be retried again and again !
                        elif code == '2':#for Decryption
                            ask_try = 'y'
                            while ask_try == 'y' or ask_try == 'Y':
                                try:
                                    Decrypt_file(password,mode,list_dirname,'',overwrite)#calling the Decrypt_file function with parameters
                                    ask_try = 'n'
                                except Exception as error:
                                    print "\nError Occured when Decrypting file :",list_dirname
                                    print error
                                    ask_try = raw_input("\nTry Again (y/n) : ")#if failed due to any reason, it can be retried again and again !
                        else:
                            print "\nError in code : it must be '1' or '2' "
                else:
                    addir = addir + subdir
                    dircount += 1
            if len(addir) == 0:
                break
            else:
                listdir = list(addir)
    else:#to avoid sub-directory encryption
        files = get_files(dirname)
        for filename in files:
            if choice == 'y' or choice == 'Y':#for Turn on run time file selection
                ask = raw_input("\nEncrypt this file : "+filename+' (y/n) ==> ')
            else:
                ask = 'y'
            if ask != 'y' and ask != 'Y':
                print "\nOk....This file is skipped ...!"
                print '-'*80
            else:
                if code == '1':#for Encryption
                    ask_try = 'y'
                    while ask_try == 'y' or ask_try == 'Y':
                        try:
                            Encrypt_file(password,mode,filename,'',overwrite)#calling the Encrypt_file function with parameters
                            filecount += 1
                            ask_try = 'n'
                        except Exception as error:
                            print "\nError Occured when Encrypting file :",filename
                            print error
                            ask_try = raw_input("\nTry Again (y/n) : ")#if failed due to any reason, it can be retried again and again !
                elif code == '2':#for Decryption
                    ask_try = 'y'
                    while ask_try == 'y' or ask_try == 'Y':
                        try:
                            Decrypt_file(password,mode,filename,'',overwrite)#calling the Decrypt_file function with parameters
                            filecount += 1
                            ask_try = 'n'
                        except Exception as error:
                            print "\nError Occured when Decrypting file :",filename
                            print error
                            ask_try = raw_input("\nTry Again (y/n) : ")#if failed due to any reason, it can be retried again and again !
                else:
                    print "\nError in code : it must be '1' or '2' "
        
    print "\nEncryption or Decryption Successful :",filecount,"files within",dircount,"Directories"


#-------------------------------------------------------Program starts----------------------------------------------------------
#taking Inputs...  
fin = raw_input("\nEnter the input file or folder Name : ")
flag = raw_input("\nEnter code ==> [1 : Encryption] & [2 : Decryption] : ")
mode = raw_input("\nEnter the Algorithm for Encryption or Decryption ==> [1: AES] & [2:DES] : ")
overwrite = raw_input("\nOverwrite the file(s) after encryption or decryption (y/n) : ")
print ''
password = getpass.getpass()#getting non-visible password
print "\nConfirm Your password...\n"
confirm = getpass.getpass()#assuring non-visible password

#if password and confirm does not matches...
while password != confirm:
    print "\nPassword Confirmation failure .... Try again ==> \n"
    password = getpass.getpass()
    print "\nConfirm Your password...\n"
    confirm = getpass.getpass()

#transforming overwrite variable to boolean
if overwrite == 'y' or overwrite == 'Y':
    overwrite = True
else:
    overwrite = False

if os.path.isfile(fin):  
    if overwrite:
        temp_path = os.path.split(fin)[0]
        fout = temp_path+"\\"+ rand_name(10)#random outfile name (which will be replaced with the actual name after encryption) for overwritting existing file
    else:
        #if the outfile name already exists...
        fout = raw_input("\nEnter the output file Name [ Default value is input file path + <adds '.enc' for encryption> or <removes '.enc' for decryption ]: ")
    print ''   
    

    if flag == '1':#for encryption
        ask_try = 'y'
        while ask_try == 'y' or ask_try == 'Y':
            try:
                Encrypt_file(password,mode,fin,fout,overwrite)#direct file encryption
                ask_try = 'n'
            except Exception as error:
                print "\nError Occured when Encrypting file :",fin
                print error
                ask_try = raw_input("\n\nTry Again (y/n) :")#try again option

    elif flag == '2':#for decryption
        ask_try = 'y'
        while ask_try == 'y' or ask_try == 'Y':
            try:
                Decrypt_file(password,mode,fin,fout,overwrite)#direct file decryption
                ask_try = 'n'
            except Exception as error:
                print "\nError Occured when Decrypting file :",fin
                print error
                ask_try = raw_input("\nTry Again (y/n) :")#try again option
                

        
elif os.path.isdir(fin):#for folder encryption
    #taking required inputs....
    level = raw_input("\nAllow subdirectory Encryption? (y/n) :")
    choice = raw_input("\nTurn on run time file selection ? (y/n) :") 
    print ''
    #transforming level variable to boolean
    if level == 'y' or overwrite == 'Y':
        level = True
    else:
        level = False
        
    Dir_Encrypt_Decrypt(fin,choice,mode,password,flag,level,overwrite)#calling the Dir_Encrypt_Decrypt function with parameters
else:
    print "\nThe given path is undefined!"

nothing = raw_input("\nEnter to Exit : ")#to pause the program after complition
    
