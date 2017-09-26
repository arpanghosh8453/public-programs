$pas = "jervis"
$count = 0
While(1)
$var = InputBox ("Arpan","password","","*")
If ($pas == $var) Then
   MsgBox (65,"Security","Authorised Person Identified")
   ExitLoop
Else
    MsgBox (21,"Security","Unauthorised Person Detected")
	$count = $count +1
 EndIf
 if ($count>4) Then
	MsgBox(16, "Too Many Attempts!!", "Get Lost!... I will close myself...", 2)
	ExitLoop
 EndIf
 
	WEnd