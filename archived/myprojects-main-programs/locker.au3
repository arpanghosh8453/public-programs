#NoTrayIcon
$pass = "Arpan"
$input = Inputbox("pass","Enter the password","","$")
If $input = $pass Then
   msgbox(64,"Correct","Thank You!!",2)
Else
   Msgbox(16,"Wrong","You can not run locker!!",2)
   Exit
EndIf
sleep(500)
$i = Inputbox("Position","Enter the path location of the file")
$a = Inputbox("Pass","Enter the pass to create","","#")
While(1)
   WinWaitActive($i)
Winclose($i)
$n = Inputbox("Pass","Enter the password to unlock","","$")
If $n = $a Then
   Exit
Else
   msgbox(16,"Wrong","Your password is wrong")
   $a = $a
EndIf


Wend