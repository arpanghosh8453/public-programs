#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Form1", 701, 501, 217, 113)
GUISetBkColor(0x99B4D1)
$L = GUICtrlCreateButton("LUDO", 48, 168, 169, 81)
$C = GUICtrlCreateButton("COIN", 464, 168, 161, 81)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###
While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 Case $L
			Run("C:\Users\Hi\Desktop\AutoIT\Compiled\Guiludo.exe")
		 Case $C
			Run("C:\Users\Hi\Desktop\AutoIT\Compiled\ProgressToss.exe")

	EndSwitch
WEnd
