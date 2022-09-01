While(1)
$t = inputbox("total","Enter the total number")
$i = InputBox("Marks","Enter your Total marks")
$r = ($i * 100)/$t
msgbox(64,"Your Percentage ",$r)
sleep(500)
$m = msgbox(36,"Query","Use Again??!!")
 if $m = 6 Then
   $r = $r
 Else
   ExitLoop
EndIf
WEnd
Exit