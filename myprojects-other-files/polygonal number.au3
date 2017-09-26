$n = inputbox("side","Enter the number of the sides of the polygon")
$e = Inputbox("Number","Enter the number of numbers")
Run("notepad.exe")
Sleep(500)
$i = ($n-1)
$d = ($n-2)
$r = 0
$x = 1
$sum = 0
If $n>1 Then
   While($r<$e)
   Send($x)
   $r = $r + 1
   $sum = ($sum + $x)
   Send(" , ")
   $x = ($x + $i)
   $i = ($i + $d)

WEnd
Send("{BACKSPACE}")
Send("{BACKSPACE}")
Send("Completed")
Send("{ENTER}")
Send("Sum of the numbers = ")
Send($sum)
Exit
Else
   msgbox(16,"Error","Wrong side number")
   Exit
EndIf

