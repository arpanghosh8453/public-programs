HotKeySet("{F2}","Function")

While(1)
WinWaitActive("Windows Task Manager")
send("{Esc}")
WEnd
Func Function()
   Exit
EndFunc   