#NoTrayIcon
HotKeySet("+S","Coin")
ProcessWaitClose("Explorer.exe")
Func Coin()
    ProgressOn("Progress starter", "Speed status : Very Fast", "0%")
    For $i = 0 To 100 Step 10
        Sleep(500)
        ProgressSet($i, $i & "%")
		if $i == 50 Then
		   ProgressSet(50, "50%Done", "Almost Complete")
	       Sleep(100)
		 EndIf
   Next
	ProgressSet(100, "100% Done", "Ready.....Please Wait")
	Sleep(2000)
    ProgressOff()
	Sleep(1000)
#include <GUIConstantsEx.au3>

GUICreate("Hello World", 1020, 680)
GUISetState(@SW_SHOW)
While(1)
;While 1
;$nMsg = GUIGetMsg()
;	Switch $nMsg
;		Case $GUI_EVENT_CLOSE
;			Exit
;	EndSwitch
;WEnd
$coin = Random(0,1,1)
if $coin == 0 Then
  $var1 = msgbox(1,"Coin Toss","You got the HEAD")
Else
   $var1 = MsgBox(1,"coin Toss","You got the TAIL")
EndIf
If $var1 == 2 Then
   Exit
EndIf
WEnd

EndFunc



