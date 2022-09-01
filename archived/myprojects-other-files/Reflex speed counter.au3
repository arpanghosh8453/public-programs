hotkeyset("^f","click")
$i = random(4,12,1)
$r = 1
$c = 0
msgbox(64,"Ready","GET READY!!",2)
sleep(1000)
Msgbox(0,"Watch","Press 'ctrl + f' when I am VANISHED!!",$i)
While($r>0)
   sleep(1)
   $c = $c + 1
WEnd
Func click()
   $r = 0
   if $c>0 Then
	  msgbox(64,"Delay time in ms",$c)
	  Exit
   Else
	  msgbox(0,"Wrong","You pressed Earlier!!")
	  Exit
   EndIf
EndFunc
