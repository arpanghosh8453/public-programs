$a = 1
$p = 0
$s = 0
$c = 0
$i = InputBox("Count","Enter the count of the numbers")
Run("C:\Program Files\Microsoft Office\Office12\EXCEL.EXE")
sleep(2000)
Send("0")
send("{RIGHT}")
While($c<$i)
   $s = $p + $a
   Send($s)
   send("{RIGHT}")
   $a = $p
   $p = $s
   $c = $c + 1
WEnd
