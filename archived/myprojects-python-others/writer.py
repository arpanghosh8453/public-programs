global increase
increase = -1
import os
import csv
os.chdir("C:\\Users\\arpan\\Desktop")

#--------------------Defining GLobals--------------------------------------------#

previousDate = "Date"
upload = 'Uploaded'
download = 'Downloaded'

#-------------------User inputs Initiated----------------------------------------#

startDate = input("Enter the starting date:")
endDate = input("Enter the ending date:")
startTime = input("Enter the starting time:")
endTime = input("Enter the ending time:")
read_filename = raw_input("Enter the input file name :")
write_filename = raw_input("Enter the output file name :")

#------------Reading input files-----------------------------------------------------#

f = file(read_filename,'r')
rf = csv.reader(f)
lrf = list(rf)
del(lrf[0])
lrf.reverse()
f1 = file(write_filename,'a')

#-----------User Defined Functions---------------------------------------------------#

def formatDate(mydate):
    if mydate == 'Date':
        return mydate
    listdate = list(mydate)
    listdate.insert(2,"/")
    listdate.insert(5, "/")
    return "".join(listdate)

def datetime(d):
    def time(t):
        if t[9] == 'P':
            hour = str(int(t[0:2])+12)
        if t[0:2] == '12' and t[9] == 'A':
            hour = '00'
        else:
            hour = t[0:2]
        tt = hour+t[3:5]+t[6:8]
        return int(tt)
    def date(dt):
        return int(dt[0:2]+dt[3:5]+dt[6:])
    datetime = d[0]
    upl = d[2]
    dnl = d[3]
    date = date(datetime[0:10])
    time = time(datetime[11:])
    return [date,time,upl,dnl]
def write(date,upload,download):
    string = formatDate(str(date))+','+str(upload)+','+str(download)+"\n"
    f1.write(string)
    return None


#--------------------------------Code Entry Point------------------------------------------#

for mysinglelist in lrf:
    mydatetime= datetime(mysinglelist)
    #print mydatetime
    if mydatetime[0] != previousDate:
        write(previousDate,upload,download)
        previousDate = mydatetime[0]
        upload = download = 0
    if mydatetime[0] >= startDate and mydatetime[0] <= endDate:
        if mydatetime[1] >= startTime and mydatetime[1] <= endTime:
            upload += int(mydatetime[2])
            download += int(mydatetime[3])

f.close()
f1.close()
