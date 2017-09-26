HotKeySet("s","start")
HotKeySet("f","finish")
msgbox(64,"Instruction","Click OK and To start the stopwatch press the s key and press the f key to stop it")
ProcessWaitClose("Explorer.exe")

Func start()
$s = 0
$m = 0
$h = 0
   While(1)
	  Sleep(1000)
	  $s = $s + 1
   WEnd
   if $s > 59 Then
	  $y = Mod($s,60)
	  $m = ($s-$y)/60
	  $s = Mod($s,60)
   ElseIf $m>59 Then
	  $x = Mod($m,60)
	  $h = ($m-$x)/60
	  $m = Mod($m,60)
   Else
	  $s = $s
   EndIf

;Func finish()

 If $h > 0 Then
   MsgBox(0,"Hour count",$h)
   MsgBox(0,"Minute count",$m)
   MsgBox(0,"Second count",$s)
 ElseIf $m>0 Then
   MsgBox(0,"Minute count",$m)
   MsgBox(0,"Second count",$s)
  ElseIf $s>0 Then
   MsgBox(0,"Second count",$s)
 Else
   MsgBox(0,"No count","Not a second")
 EndIf
Exit
;EndFunc
EndFunc

