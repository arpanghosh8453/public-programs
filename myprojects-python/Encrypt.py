import os, random, struct,hashlib,getpass,glob
from Crypto.Cipher import AES

def encrypt_file(password, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    key =  hashlib.sha256(password).digest()
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(password, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    key =  hashlib.sha256(password).digest()
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

choice = raw_input("Enter the Correct code [ File : 1 & Folder : 2 ] : ")
path = raw_input("Enter the full path for it : ")
ask = raw_input("Enter the Correct code [ Encryption : 1 & Decryption : 2 ] : ")
password = getpass.getpass()

if ask == '1':
    if choice == '1':
        encrypt_file(password,path)
    elif choice == '2':
        filelist = glob.glob(path+'\\*.*')
        os.mkdir(path+'\\Encrypted')
        for filedir in filelist:
            newpath = path+'\\Encrypted\\'+filedir.split('\\')[-1]+'.enc'
            print "Encrypting",filedir
            encrypt_file(password,filedir,newpath)
    else:
        print "Error Occured ! "
elif ask == '2':
    if choice == '1':
        decrypt_file(password,path)
    elif choice == '2':
        filelist = glob.glob(path+'\\*.*')
        os.mkdir(path+'\\Decrypted')
        for filedir in filelist:
            newpath = path+'\\Decrypted\\'+filedir.split('\\')[-1]
            outfile = os.path.splitext(newpath)[0]
            print "Decrypting",filedir
            decrypt_file(password,filedir,outfile)
    else:
        print "Error Occured ! "
