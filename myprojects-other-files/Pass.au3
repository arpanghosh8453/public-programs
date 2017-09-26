$pas = "jervis"
$var = InputBox ("Arpan","password","","*")
If ($pas == $var) Then
   MsgBox (0,"Security","Authorised Person Identified")
Else
    MsgBox (0,"Security","Unauthorised Person Detected")
	EndIf