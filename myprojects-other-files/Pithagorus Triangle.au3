$i = InputBox("count","Enter The Number")
$n = 4
$c = 0
Run("notepad.exe")
sleep(2000)
While($i>$c)
   if Mod($n,2) = 0 Then
	  $f = (($n * $n)/4)-1
	  $l = ($f + 2)
   Else
	  $f = (($n * $n)-1)/2
	  $l = ($f + 1)
   EndIf
   $n2 = $n*$n
   $f2 = $f*$f
   $l2 = $l*$l
   send($n2)
   send("(")
   send($n)
   send(")")
   send(" ")
   send("+")
   send(" ")
   send($f2)
   send("(")
   send($f)
   send(")")
   send(" ")
   send("=")
   send(" ")
   send($l2)
   send("(")
    send($l)
   send(")")
   send("{ENTER}")
   $n = ($n + 1)
   $c = ($c+1)
WEnd
Exit
