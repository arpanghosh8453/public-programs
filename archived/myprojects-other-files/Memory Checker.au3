While(1)
$i = random(1,2)
$l = -4
While($l<10)
   $i = $i * 10
   $l = ($l + 1)
   WEnd
msgbox(64,"Get Ready","Get Ready")
sleep(1000)
msgbox(64,"Look",$i,10)
sleep(6000)
$n = InputBox("Enter ","Enter The Number Now")
$m = 0
While($i>0)
   $m1 = Mod($i,10)
   $m2 = Mod($n,10)
   If $m1 = $m2 Then
	  $m = ($m + 1)
   Else
	  $m = $m
   EndIf
   $i = ($i-$m1)/10
   $n = ($n-$m2)/10
   WEnd
if $n = $i Then
   Msgbox(64,"WIN","Your Memory is WONDERFUL!!")
     Elseif $m<3 Then
     Msgbox(16,"lost","Your Memory is TOO LOW!!")
	 Elseif $m>2 And $m<6 Then
	 msgbox(64,"Progress","You have an average memory")
	 Elseif $m>5 and $m<10 Then
	 Msgbox(64,"Progress","You have a good memory")
  Else
	 Msgbox(16,"Dull","Go to a Doctor")
  EndIf
  sleep(500)
 $m =  msgbox(36,"Query","Use it Again??!!")
  if $m = 6 Then
	 $i = $i
  Else
	 ExitLoop
  EndIf
  WEnd
  Exit