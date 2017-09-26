While(1)
$i = InputBox("Decimal","Enter the Number in Decimal")
if Mod($i,2) = 0 Then
   $n = $i+1
Else
   $n = $i
EndIf
$s = 0
While($n>0)
   $r = Mod($n,2)
   $n = ($n-$r)/2
   $s = $s + $r
   $s = $s * 10
WEnd
$s = $s/10
$a = $s
$b = 1
While($a>1)
   $x = Mod($a,10)
   $a = ($a-$x)/10
   $b = $b * 10
WEnd
$t = 0
While($s>0)
   $c = Mod($s,10)
   $s = ($s-$c)/10
   $d = $c * $b
   $b = $b/10
   $t = $t + $d
WEnd
If Mod($i,2) = 0 Then
   $t = $t-1
Else
   $t = $t
EndIf
MsgBox(0,"Binary Digit",$t)
sleep(200)
$m = MsgBox(36,"Query","Use Again??!")
if $m = 6 Then
   $i = 0
Else
   Exit
EndIf
WEnd