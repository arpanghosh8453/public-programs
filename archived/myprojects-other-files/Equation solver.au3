while(1)
MsgBox(64,"instruction","Enter the values of a,b & c in the ax^2 + bx + c = 0 in the following Inputboxes")
$a = Inputbox("a","Enter the value of a :")
$b = Inputbox("b","Enter the value of b :")
$c = Inputbox("c","Enter the value of c :")
$b = ($b*(-1))
$x = ($b * $b)- (4*($a * $c))
If $x>0 then
   MsgBox(64,"type of Values","Real & Unequal")
   Elseif $x = 0 Then
    MsgBox(64,"type of Values","Real & Equal")
 Else
	MsgBox(64,"type of Values","Imaginary Values")
	Exit
 EndIf
 $x = sqrt($x)
 $r1 = ($b+$x)/(2*$a)
 $r2 = ($b-$x)/(2*$a)
 msgbox(64,"Bigger value of x",$r1)
 msgbox(64,"Smaller value of x",$r2)
 sleep(500)
 $m = msgbox(36,"Query","Use Again??!!")
 if $m = 6 Then
   $a = $a
 Else
   ExitLoop
EndIf
WEnd
Exit
