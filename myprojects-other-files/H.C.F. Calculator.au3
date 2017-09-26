$i = InputBox("Number","Enter the First Number")
$r = $i
$d = $i
While (1)
   $a = MsgBox(36,"Qwery","Input More Numbers??!")
   If $a = 6 Then
	  $r = $r
   Else
	  MsgBox(64,"H.C.F. Result",$r)
	  Exit
   EndIf
   $n = InputBox("Number","Enter The Next Number")
   if $n>$r Then
	  $g = $n
	  $d = $r
   Else
	  $g = $d
	  $d = $n
   EndIf
   While(1)
	  $e = Mod($g,$d)
	  If $e = 0 Then
		 $r = $d
		 ExitLoop
	  Else
		 $g = $d
		 $d = $e
	  EndIf
   WEnd
WEnd
