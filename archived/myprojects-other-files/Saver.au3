#include <GUIConstantsEx.au3>
#NoTrayIcon
GUICreate("Hello World", 200, 1000) 
GUISetState(@SW_SHOW)
$var = "Jervis"
While(1)
$pas = InputBox("Password","Authenticating the user","","$")
 If $var == $pas Then
   MsgBox(64,"Message","Thank You",2)
   Exit
 Else
   MsgBox(16,"Message","Wrong Attempt",2)
   Run("C:\Users\Hi\Desktop\AutoIT\Compiled\close.exe") 
   Exit
EndIf
WEnd