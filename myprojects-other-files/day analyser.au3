$y = InputBox("year","Enter the year")
$m = InputBox("Month","Enter the month number")
$d = InputBox("date","Enter the date")
if $y=0 or $y<0 Then
   Msgbox(16,"Error","Invalid year,Month or date")
   Exit
ElseIf $m=0 or $m<0 Then
   Msgbox(16,"Error","Invalid year,Month or date")
   Exit
ElseIf $m>12 Then
   Msgbox(16,"Error","Invalid year,Month or date")
   Exit
ElseIf $d>31 Then
   Msgbox(16,"Error","Invalid year,Month or date")
   Exit
ElseIf $d=0 or $d<0 then
   Msgbox(16,"Error","Invalid year,Month or date")
   Exit
Else
   $d = $d
EndIf
$y1 = $y
If mod($y1,100)= 0 Then
   $y1= $y1/100
   Else
   $y1 = $y1
EndIf
If mod ($y1,4) = 0 Then
   $ly = 1
Else
   $ly = 0
EndIf
If $m = 1 And $ly = 0 Then
   $m = 1
ElseIf $m = 1 And $ly = 1 Then
   $m = 0
ElseIf $m = 1 And $ly = 1 Then
   $m = 0
ElseIf $m = 2 And $ly = 1 Then
   $m = 3
ElseIf $m = 2 And $ly = 0 Then
   $m = 4
ElseIf $m = 3 or $m = 11 Then
   $m = 4
ElseIf $m = 4 or $m = 7 Then
   $m = 0
ElseIf $m = 5 Then
   $m = 2
ElseIf $m = 6 Then
   $m = 5
ElseIf $m = 8 Then
   $m = 3
ElseIf $m = 9 or $m = 12 Then
   $m = 6
ElseIf $m = 10 Then
   $m = 1
Else
   Exit
EndIf
$ye = mod($y,100)
$a = mod($ye,4)
$yp = ($ye - $a)/4
$ys = ($y - $ye)/100
$n = mod($ys,4)
If $n = 1 Then
   $l = 4
elseif $n = 2 Then
   $l = 2
Elseif $n = 3 Then
   $l = 0
Else
   $l = 6
EndIf
$sum = ($ye + $yp + $m + $d + $l)
$r = mod($sum,7)
if $r = 0 Then
   msgbox(64,"Day","It is SATURDAY!")
ELSEif $r = 1 Then
   msgbox(64,"Day","It is SUNDAY!")
ELSEif $r = 2 Then
   msgbox(64,"Day","It is MONDAY!")
ELSEif $r = 3 Then
   msgbox(64,"Day","It is TUESDAY!")
ELSEif $r = 4 Then
   msgbox(64,"Day","It is WEDNESDAY!")
   ELSEif $r = 5 Then
   msgbox(64,"Day","It is THURSDAY!")
ELSEif $r = 6 Then
   msgbox(64,"Day","It is FRIDAY")
Else
   Exit
EndIf
Exit