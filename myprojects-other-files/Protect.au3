
#include <GUIConstantsEx.au3>

GUICreate("Hello World", 2000, 1000) 
GUISetState(@SW_SHOW)
$var = "Jervis"
$num = "0"
While(1)
  $pas = InputBox("Password","Verifying","","#")
If $var == $pas Then
	 
	 Exit
	 
  Else
	 $num = $num+1
  EndIf
if $num>6 Then
   ExitLoop
EndIf
WEnd

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
 Case $GUI_EVENT_CLOSE
   
	
			

	EndSwitch
WEnd