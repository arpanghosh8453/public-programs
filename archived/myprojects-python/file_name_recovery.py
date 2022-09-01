import os,csv
infile = open("C:\\rename\\list.csv",'r')
mylist = list(csv.reader(infile))
for sublist in mylist:
    try:
        os.rename(sublist[1],sublist[0])
        print "SUCCESS :",sublist
    except Exception as error:
        print "FAILURE :",sublist,"due to",str(error)
        
