
HotKeySet("^m","Start")
$h = InputBox("hour","Enter the hour Value")
$m = InputBox("Minute","Enter the Minute Value")
$s = InputBox("Second","Enter the Second Value")
ProcessWaitClose("Explorer.exe")
Func Start()
   msgbox(64,"start","Your time starts now!!",1)
   $s = $s + ($h * 3600)+($m*60)
   $w = 0
   sleep($s * 1000)
   msgbox(64,"End","Your time is UP!!",2)
   Exit
EndFunc
