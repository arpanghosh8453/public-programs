$s=InputBox("start","Input The Starting Number")
$e=InputBox("End","Input The Ending Number")
$r = 0
$w = 0
$e = $e + 1
run("C:\Program Files\Microsoft Office\Office12\EXCEL.EXE")
      Sleep(2000)
While($s<4)
   If $s = 0 then
	  MsgBox(0,"Error","Cannot define 0!!")
	  ElseIf $s = 1 then
	  MsgBox(0,"Error","Cannot define 1!!")
   ElseIf $s = 2 or $s = 3 Then
	  send($s)
	 send("{RIGHT}")
	 $r = $r + 1
  Else
	$s = $s * 1
  EndIf
  $s = $s + 1
  WEnd
  While($e>$s)
	 If mod($s,2) = 0 then
		$s = $s * 1
	 Else
		$a = 3
		$x = Mod($s,2)
		$y = (($s-$x)/2)+2
		While($y>$a)
		   If mod($s,$a) = 0 then
			  $w = 0
			  Exitloop
		   Else
			  $w = 1
			  $a = $a +2
		   EndIf
		WEnd
		if $w = 1 Then
		   send($s)
		   send("{RIGHT}")
	   $r = $r + 1
		Else
		   $s = $s * 1
		EndIf
	 EndIf
	 $s = $s + 1
  WEnd
  ProcessWaitClose("EXCEL.EXE")
If $r = 0 Then
	 MsgBox(48,"Sorry","No Prime Numbers Found....")
	 Exit
  Else
	 msgbox(64,"Total Count",$r)
	 Exit
  EndIf
