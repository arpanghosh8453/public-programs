#include <GUIConstantsEx.au3>

GUICreate("Hello World", 2000, 1000) 
GUISetState(@SW_SHOW)
$pass = "Jervis"
While 1
$var = InputBox("password","pass","","$")

if $var == $pass Then
   Exit
EndIf
WEnd

