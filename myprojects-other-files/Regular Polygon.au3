msgbox(64,"Instruction","Type 1,2 or 3 respectively toenter the internal angle,External angle or the number of sides in the regular polygon")
$c = inputbox("choice","Enter your Choice")
if $c = 1 Then
   $i = inputbox("angle","Enter the Internal angle")
   $e = $i
   $x = (180-$i)
   $n = (360/$x)
Elseif $c = 2 Then
$i = inputbox("angle","Enter the External angle")
   $x = $i
   $e = (180-$i)
   $n = (360/$x)
ElseIf $c = 3 Then
   $i = inputbox("Side","Enter the number of sides of the polygon")
   $n = $i
   $x = (360/$n)
   $e = (180-$x)
Else
   msgbox(16,"Error","Wrong Choice")
   Exit
EndIf
msgbox(64,"Internal Angle",$e)
msgbox(64,"External Angle",$x)
msgbox(64,"number of sides",$n)
Exit