While(1)
$result = 1
$var = 0
$input = InputBox("Factorial","Type A Correct Number")
If $input>0 Then
   While($var<$input)
	  $var = $var + 1
	  $result = $result * $var
   WEnd
   MsgBox(64,"Result",$result)
Else
   MsgBox(16,"Error","Input A Correct Number")
EndIf
sleep(200)
$m = msgbox(36,"Query","Use Again??!")
If $m = 6 Then
   $result = $result
Else
   Exit
EndIf
Wend
