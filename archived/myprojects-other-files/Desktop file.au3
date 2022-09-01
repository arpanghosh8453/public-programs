#include <File.au3>
$n = InputBox("Input","Enter Anything")
_FileCreate ("C:\Users\Hi\Desktop\new.ini")
FileOpen("C:\Users\Hi\Desktop\new.ini",1)
FileWrite("C:\Users\Hi\Desktop\new.ini",$n)
$p = FileRead("C:\Users\Hi\Desktop\new.ini")
send($p)