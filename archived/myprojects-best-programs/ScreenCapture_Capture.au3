#NoTrayIcon
#include <ScreenCapture.au3>

Example()

Func Example()
   DirCreate("D:\Backup\pictures")
   $foldernum = 1
   $folder = "D:\Backup\pictures\" & $foldernum
   $numindex = 1
   While FileExists($folder)
	  $foldernum = $foldernum + 1
	  $folder = "D:\Backup\pictures\" & $foldernum
   WEnd
   DirCreate($folder)
   while (1)
	  $name = "Picture" & $numindex
	  sleep(30000)
	  _ScreenCapture_Capture($folder & "\" & $name & ".jpg")
	  $numindex = $numindex + 1
	WEnd
EndFunc