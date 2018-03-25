import os,glob
print "\n**Please shorten the name to get correct results...make sure that your filename does not contain any space,dot,comma etc to avoid errors...Skip the output file if needed\n"
ask = raw_input("File or folder : ")
if ask == "file":
    fin = raw_input("Enter the inpute file :")
    fout = raw_input("Enter the output file : ")
    if fout == '':
        l = fin.split('.')
        fout = l[0]+'.mp4'
    string = r"C:\ffmpeg\bin\ffmpeg.exe -i "+fin+" "+fout
    #print string
    os.system(string)
else:
    foin = raw_input("Enter the inpute folder :")
    for i in glob.glob(foin+"\*.*"):
        fin = i
        fout = ''
        if fout == '':
            l = fin.split('.')
            fout = l[0]+'.mp4'
        string = r"C:\ffmpeg\bin\ffmpeg.exe -i "+fin+" "+fout
        #print string
        os.system(string)
