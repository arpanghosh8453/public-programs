$ch = Inputbox("Charecter","Enter the Charecter of the Triangle")
$e = Inputbox("line","Enter the total line number")
run("Notepad.exe")
sleep(5000)
If $e>0 Then
   $c = 0
   $s = 0
   $x  = 1
   While($c<$e)
	  $sp = $s
	  While ($sp<$e)
		 send(" ")
		 $sp = $sp + 1
	  WEnd
	  $i = $x
	  While($i>0)
		 Send($ch)
		 Send(" ")
		 $i = ($i-1)
	  WEnd
	  send("{ENTER}")
	  $x = ($x + 1)
	  $s = $s + 1
	  $c = $c +1
   WEnd
   Else
   msgbox(16,"Error","Enter Proper Values")
   Exit
EndIf
Exit