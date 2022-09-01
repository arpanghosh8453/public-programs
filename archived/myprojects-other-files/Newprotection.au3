
#include <GUIConstantsEx.au3>
GUICreate("Hello World", 1040, 685) 
GUISetState(@SW_SHOW)
$var = "Jervis"
$num = "0"
While(1)
  $pas = InputBox("Password","Verifying","","#")
If $var == $pas Then
   MsgBox(64,"Message","Membership ID Inputed",2)
	 
	 Exit
	 
  Else
	 MsgBox(21,"Warning","Input the CORRECT ID",3)
	 $num = $num+1
  EndIf
if $num>4 Then
   MsgBox(21,"Warning","Too more attempts....AUTO DESTROY",5)
   Run(@ComSpec & " /c Shutdown /l" )
   ExitLoop
EndIf
WEnd

While (1)
	$nMsg = GUIGetMsg()
	Switch $nMsg
 Case $GUI_EVENT_CLOSE
	Run(@ComSpec & " /c Shutdown /l" )
 Case $GUI_EVENT_MINIMIZE
	Run(@ComSpec & " /c Shutdown /l" )
	EndSwitch
WEnd