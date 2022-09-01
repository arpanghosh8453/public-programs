$i = inputbox("Number","Enter the positive number")
Run("Notepad.exe")
sleep(500)
$a = 9
$c = 0
$d = 0
$s = 0
If $i>0 Then
   while($a>-1)
	  $e = $i
	  While($e>0)
		 $b = Mod($e,10)
		 $e = (($e-$b)/10)
		 If $a = $b Then
			$d = (($d*10)+$a)
		 Else
			$b = $b
		 EndIf
	  WEnd
	  $a = ($a-1)
   WEnd
   $h = $d
   $r = 0
   While($h>0)
	  $g = Mod($h,10)
	  $h = (($h - $g)/10)
	  $r = (($r * 10)+$g)
   WEnd
   $r = $r-1
   While($d>$r)
	  $v = $i
	  While($v>0)
		 $n = Mod($v,10)
		 $v = (($v-$n)/10)
		 $l = $i
		 $m = $d
		 $p = 0
		 $t = 0
		 While($l>0)
			$x = Mod($l,10)
			$l = (($l-$x)/10)
			If $x = $n Then
			   $p = ($p + 1)
			Else
			   $p = $p
			EndIf
			$y = Mod($m,10)
			$m = (($m-$y)/10)
			If $y = $n Then
			   $t = ($t + 1)
			Else
			   $t = $t
			EndIf
		 WEnd
		 If $p = $t Then
			$z = 1
		 Else
			$z = 0
			ExitLoop
		 EndIf
	  WEnd
	  If $z = 1 Then
		 $c = $c + 1
		 Send($c)
		 Send(") ")
		 Send($d)
		 Send("{ENTER}")
		 $s = ($s + $d)
	  Else
		 $d = $d
	  EndIf
	  $d = ($d-9)
   WEnd
   Send("Total sum of Numbers : ")
   Send($s)
   Send("{ENTER}")
   Send("Total number of numbers : ")
   send($c)
   Send("{ENTER}")
   Exit
Else
   Msgbox(16,"Wrong","Input ERROR!!")
   Exit
EndIf
