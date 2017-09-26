$l = InputBox("lengtgh","Enter the length ")
$b = InputBox("Breath","Enter the Breath ")
$ch = InputBox("Charecter","Enter the Charecter ")
$b1 = 0
Run("Notepad.exe")
sleep(1000)
While($b1<$b)
   $l1 = 0
   While($l1<$l)
	  send($ch)
	  send(" ")
	  $l1 = ($l1+1)
   WEnd
   send("{ENTER}")
   $b1 = ($b1+1)
WEnd
Exit