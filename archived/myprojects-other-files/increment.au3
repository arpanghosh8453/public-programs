$s = InputBox(0,"Input The Starting Number")
$e = InputBox(0,"Input The Ending Number")
$i = Inputbox(0,"Input The Increment Value")
$e = $e + 1
run("notepad.exe")
sleep(1000)
While($e>$s)
   send($s)
   Send(" , ")
   $s = ($s + $i)
WEnd
Msgbox(64,"prompt","Completed")
Exit
