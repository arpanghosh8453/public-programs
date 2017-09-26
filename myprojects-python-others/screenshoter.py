import datetime , time , pyscreenshot , ctypes
try:
    os.mkdir("C:\\screenshots")
except:
    pass
ctypes.windll.kernel32.SetFileAttributesW(ur'C:\\screenshots',2)


if  __name__ == "__main__":
    while True:
        path = 'C:\\screenshots\\'+datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")+'.jpg'
        pyscreenshot.grab_to_file(path)
        print "Done in "+path
        time.sleep(300)   
