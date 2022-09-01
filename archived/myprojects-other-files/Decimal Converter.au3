While(1)
$i = InputBox("Binary","Enter the Number in Binary")
if $i<10 Then
   MsgBox(64,"Decimal Value",$i)
Elseif Mod($i,2)=0 Then
   $n = $i+1
Else
   $n = $i
EndIf
$a = $n
$b = 1
While($a>0)
    $p = Mod($a,10)
	$a = ($a-$p)/10
	$b = $b * 10
WEnd
$b = $b/10
$s = 0
While($n>0)
   $c = Mod($n,10)
   $p = Mod($n,10)
   $n = ($n-$p)/10
   $r = $c * $b
   $b = $b / 10
   $s = $s + $r
WEnd
$x = 0
While($s>0)
   $d = Mod($s,10)
   $s = ($s-$d)/10
   $x = ($x * 2)+$d
WEnd
If Mod($i,2) = 0 Then
   $x = $x-1
Else
   $x = $x
EndIf
MsgBox(0,"Binary Digit",$x)
sleep(200)
$m = MsgBox(36,"Query","Use Again??!")
if $m = 6 Then
   $i = 0
Else
   Exit
EndIf
WEnd