while(1)
   msgbox(64,"Instruction"," To enter the degree value   ")
   $c = Inputbox("choice","Enter Your choice")
   $i = Inputbox("value","Enter the value of the Angle")
   If $c = 2 Then
	  $r = (1260 * $i)/22
	  msgbox(64,"Degree Value",$r)
   ElseIf $c = 1 then
	  $r = (22*$i)/1260
	  msgbox(64,"Radian Value",$r)
   Else
	  msgbox(16,"Error","Wrong choice")
	  Exit
   EndIf
   sleep(500)
   $m = msgbox(36,"Query","Use Again??!!")
 if $m = 6 Then
   $r = $r
 Else
   ExitLoop
EndIf
WEnd
Exit
