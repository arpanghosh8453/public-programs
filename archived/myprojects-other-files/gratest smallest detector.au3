#include <Math.au3>
$i = InputBox("Number","Enter the first Number")
$g = $i
$s = $i
While(1)
   $n= InputBox("Number","Enter the next number")
   If $n>$g Then
	  $g = $n
   Else
	  $g = $g
   EndIf
   If $n<$s then
	  $s = $n
   Else
	  $s = $s
   EndIf
   Sleep(200)
   $d = Msgbox(36,"Query","Input More Numbers??")
   If $d = 6 Then
	  $n = $n
   Else
	  ExitLoop
   EndIf
WEnd
Msgbox(64,"Maximum Value",$g)
Msgbox(64,"Minimum Value",$s)
Exit


