$s = inputbox("number","Enter the starting number")
$e = Inputbox("End","Enter the ending number")
$e = ($e + 1)
If $e>1 And $e>$s Then
   Run("Notepad.exe")
   Sleep(500)
Else
   Msgbox(16,"Error","Wrong values")
   Exit
EndIf
While($s<$e)
   $p = 0
   $c = $s
   While($c>0)
	  $n=Mod($c,10)
	  $c = ($c-$n)/10
	  $p = $p+$n
   WEnd
   IF Mod($s,$p) = 0 Then
	  Send($s)
	  Send(" , ")
	  $s = $s + 1
   Else
	  $s = $s + 1
   EndIf
WEnd
Send("COMPLETED")
Exit