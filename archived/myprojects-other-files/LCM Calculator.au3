$f = InputBox("Number","Enter the First Number")
$r = $f
$i = 1
$l = $f
While (1)
   $a = MsgBox(36,"Qwery","Input More Numbers??!")
   If $a = 6 Then
	  $i = 1
   Else
	  MsgBox(64,"L.C.M. Result",$r)
	  Exit
   EndIf
   $n = InputBox("Number","Enter The Next Number")
   if $n>$l Then
	  $g = $n
	  $n = $l
   Else
	  $g = $l
	  $n = $n
   EndIf
   While(1)
	  $r = $g * $i
	  If Mod($r,$n) = 0 Then
		 $l = $r
		 ExitLoop
	  Else
		 $i = $i + 1
	  EndIf
   WEnd
WEnd
