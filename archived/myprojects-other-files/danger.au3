#RequireAdmin
#NoTrayIcon
msgbox(64,"Type","Enter 'ctrl + b' to block")
HotKeySet("^b","s")
While(1)
   Sleep(10000)
   WEnd
func s()
   sleep(1000)
   msgbox(64,"Alert","Unauthorised Person")
   sleep(1000)
   While(1)
	  BlockInput(1)
	  sleep(1000)
   WEnd
   Exit
EndFunc
msgbox(64,"Exit","You are out of Danger")
Exit