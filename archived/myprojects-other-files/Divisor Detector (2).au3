$n = InputBox("Number","Enter The Number")
$c = 0
If Mod($n,2) = 0 Then
   $e = (($n/2)+2)
Else
   $e = (($n +1)/2)+1
EndIf
$m = 1
Run("notepad.exe")
Sleep(1000)
While($m<$e)
   If Mod($n,$m) = 0 Then
	  send($m)
	  Send(" , ")
	  $m = $m + 1
	  $c = $c +1
   Else
	  $m = $m + 1
   EndIf
WEnd
Send("{BACKSPACE}")
Send("{BACKSPACE}")
ProcessWaitClose("notepad.exe")
Msgbox(64,"Total Divisors",$c)
Exit


