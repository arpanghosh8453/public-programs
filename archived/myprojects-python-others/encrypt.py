import binhex
import time
password = 'bonisona'
youpass = input("Enter the password :")
if password != youpass:
    print('Wrong password ....Aborting...')
    time.sleep(5)
    exit()
else:
    infilename = str(input("Enter the infile name :"))
    outfilename = str(input("Enter the outfile name :"))
    binhex.binhex(infilename,outfilename)





 
