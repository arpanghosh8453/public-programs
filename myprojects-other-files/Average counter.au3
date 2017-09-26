$i = InputBox("Input","Enter The First Number")
$s = $i
$d = 1
While(1)
   $m = MsgBox(36,"Query","Input More Numbers??!")
   If $m = 6 Then
	  $n = InputBox("Input","Enter The Next Number")
	  $s = $s + $n
	  $d = $d + 1
   Else
	  $r = $s/$d
	  MsgBox(64,"Net Average",$r)
	  ExitLoop
   EndIf
WEnd
Exit