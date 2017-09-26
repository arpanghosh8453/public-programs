#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Form1", 700, 400, 220, 200)
$Button1 = GUICtrlCreateButton("Button1", 96, 216, 75, 25)
$Button2 = GUICtrlCreateButton("Button2", 320, 216, 75, 25)
$Label1 = GUICtrlCreateLabel("", 20, 64, 500, 104)
GUICtrlSetFont(-1, 19, 800, 4, "Verdana")
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0x99B4D1)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 Case $Button1
			GUICtrlSetData($Label1, "BoniSona Baro Bhalo Chele")
		 case $Button2
			GUICtrlSetData($Label1,"")

	EndSwitch
WEnd
