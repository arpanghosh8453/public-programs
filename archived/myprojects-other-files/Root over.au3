$n = Inputbox("Number","Enter the number")
$p = Inputbox("Power","Enter the root power")
$d = Inputbox("Decimal","Enter the count of Decimalplaces")
$c = $n
$k = 0
While($c>0)
   $m = Mod($c,10)
   $c = (($c-$m)/10)
   $k = ($k + 1)
WEnd
$g = Mod($k,$p)
$k = ($k+($k-$g))/$p
$i = 1
$s = 0
While($k>$s)
   $i = ($i*10)
   $s = ($s + 1)
WEnd
$x = 0
$e = (-2)+((-1)* $k)
If $n>0 And $d<10 Then
   While($e<$d)
	  $a = $x
	  $b = 1
	  While($p>$b)
		 $a = $a * $a
		 $b = ($b + 1)
	  WEnd
	  If $a>$n Then
		 $x = ($x-$i)
		 $i = ($i * 0.1)
		 $e = ($e + 1)
	  ElseIf $a = $n Then
		 ExitLoop
	  Else
		 $x = $x
	  EndIf
	  $x = ($x+$i)
   WEnd
   $x = Round($x,$d)
   Msgbox(64,"Root of Numbers",$x)
   Exit
Else
   Msgbox(16,"Wrong","Enter Proper Values!!")
   Exit
EndIf
