$n = Inputbox("Base","Enter the base number of the Triangle")
$e = Inputbox("line","Enter the total line number")
run("notepad.exe")
sleep(1000)
if $e>0 Then
   $c = 0
   $s = 0
   $sum = 0
   While($c<$e)
	  $sp = $s
	  While ($sp<$e)
		 send(" ")
		 $sp = $sp + 1
	  WEnd
	  $l = 0
	  $x = $n
	  $i = 1
	  $d = 2
	  Send("1 , ")
	  While($l<$n)
		 send($x)
		 $sum = ($sum + $x)
		 Send(" , ")
		 $x = $x * (($n-$i)/$d)
		 $d = ($d+1)
		 $i = ($i +1)
		 $l = ($l+1)
	  WEnd
	  Send("{BACKSPACE}")
	  Send("{BACKSPACE}")
	  send("{ENTER}")
	  $n = ($n + 1)
	  $s = $s + 1
	  $c = $c +1
   WEnd
   $sum = $sum + $e
   send("Total sum of Numbers = ")
   Send($sum)
   Exit
Else
   msgbox(16,"Error","Enter Proper Values")
   Exit
EndIf
Exit