While(1)
   $i = InputBox("Price","Input The Printed Price")
   $d = InputBox("discount","Input The Discount In Percent")
   $r = $i - ($i*($d/100))
   Sleep(200)
   MsgBox(64,"Result",$r)
   Sleep(200)
   $m = MsgBox(36,"Query","Use Again??")
   If $m = 6 Then
	  $r = 0
   Elseif $m = 7 Then
      Exit
   Else
	  Exit
   EndIf
   WEnd