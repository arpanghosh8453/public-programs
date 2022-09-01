HotKeySet("c","C")
HotKeySet("f","F")
MsgBox(0,"Prompt","Press c to start Fahrenheit to Centigrade Conversation or Press f to start Centigrade to fahrenheit Conversation and press ok")
func C()
   $f = InputBox("fahrenheit","Input the Tempareture value in fahrenheit")
   $c = ((5 * $f)-160)/9
   MsgBox(64,"Your centigrade value",$c)
   $m = msgbox(36,"Query","Use Again??!")
   if $m = 6 Then
	  MsgBox(0,"Prompt","Press c to start Fahrenheit to Centigrade Conversation or Press f to start Centigrade to fahrenheit Conversation and press ok")
   ProcesswaitClose("Explorer.exe")
   Else
   EndIf
EndFunc
Func F()
  $c = InputBox("Centigrade","Input the Tempareture value in Centigrade")
   $f = ((5 * $c)-160)/9
   MsgBox(64,"Your Fahrenheit value",$f)
   $m = msgbox(36,"Query","Use Again??!")
   if $m = 6 Then
	  MsgBox(0,"Prompt","Press c to start Fahrenheit to Centigrade Conversation or Press f to start Centigrade to fahrenheit Conversation and press ok")
	  ProcesswaitClose("Explorer.exe")
   Else
	  Exit
   EndIf
EndFunc
