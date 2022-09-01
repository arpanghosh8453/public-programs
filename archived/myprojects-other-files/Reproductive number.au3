$i = Inputbox("Number","Enter the number of Numbers")
$c = 0
$s = 0
$x = InputBox("start","Enter the Starting number")
$a = inputbox("increment","Enter the multiplier increment value")
run("notepad.exe")
sleep(1000)
While($c<$i)
   send($x)
   $s = ($s+$x)
   send(" ,")
   $x = ($a * $x)
   $c = $c + 1
WEnd
send("Completed")
Send("{ENTER}")
Send("Total = ")
send($s)
Exit