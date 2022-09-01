from PIL import Image
import os,glob

path = input("Enter the folder path : ")
increase = 1
os.mkdir(path+"\Converted_files")
for string in glob.glob(path+"\*.jpg"):
    name = "Image_"+str(increase)
    foo = Image.open(string)
    width,height = foo.size
    print ("Working with ... ",name)
    foo = foo.resize((width//2,height//2),Image.ANTIALIAS)
    foo.save(path+"\Converted_files\\"+name+".jpg",optimize=True,quality=95)
    print ("completed : ",name)
    increase += 1
