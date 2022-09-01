#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#include <GuiButton.au3>

global $flag = 0
Global $d = TimerInit()
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("", 743, 492, 157, 132)
GUISetFont(36, 800, 0, "Arial Narrow")
GUISetBkColor(0x99B4D1)
$Label1 = GUICtrlCreateLabel("Casino", 272, 24, 168, 73)
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0xA0A0A4)
$a = GUICtrlCreateLabel("00", 42, 120, 154, 108)
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0x00FFFF)
$b = GUICtrlCreateLabel("00", 280, 120, 170, 108)
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0x00FFFF)
$c = GUICtrlCreateLabel("00", 552, 120, 146, 108)
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0x00FFFF)
$Button1 = GUICtrlCreateButton("Start", 72, 304, 225, 89)
GUICtrlSetFont(-1, 36, 800, 0, "Arial")
GUICtrlSetColor(-1, 0x800000)
GUICtrlSetBkColor(-1, 0x00FF00)
$Button2 = GUICtrlCreateButton("STOP", 400, 304, 225, 89)
GUICtrlSetColor(-1, 0xFFFF00)
GUICtrlSetBkColor(-1, 0xFF0000)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###
_GUICtrlButton_Enable ($Button2,False)
loop()

func loop()

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 Case $Button1

			start()

		 Case $Button2

			stop()
			$d = 0

	EndSwitch
 WEnd
 EndFunc

 func start()
	Local $d
	local $i
	_GUICtrlButton_Enable ($Button1,False)
	_GUICtrlButton_Enable ($Button2,True)
	While(1)
	   $m = GUIGetMsg()
	   if TimerDiff($d)>20 Then
	$av = random(00,09,1)
	$bv = random(00,09,1)
    $cv = random(00,09,1)
	GUICtrlSetData($a,$av)
	GUICtrlSetData($b,$bv)
	GUICtrlSetData($c,$cv)
	$d = TimerInit()
	EndIf
   Select
	case $m = $Button2
	   stop()
    Case $m = $GUI_EVENT_CLOSE
			Exit
	EndSelect


	WEnd

 EndFunc
 func stop()

	_GUICtrlButton_Enable ($Button2,False)
	_GUICtrlButton_Enable ($Button1,True)
	$p = 1
	while(1)
    $m = GUIGetMsg()
	$aa = GUICtrlRead($a)
	$bb = GUICtrlRead($b)
	$cc = GUICtrlRead($c)
	Select
	case $m = $Button1
	   start()
    Case $m = $GUI_EVENT_CLOSE
			Exit
	EndSelect
	If $p = 1 Then
	if $aa = $bb And $aa = $cc Then
	   Msgbox(64,"Win","You Won The Cup!!")
	ElseIf $aa = $bb Or $aa = $cc Or $bb = $cc Then
	    Msgbox(64,"Win","You Won a small Prize!!")
	 Else
		Msgbox(16,"Sorry","Nothing Mached!!")
	 EndIf
	 $p = 2
  Else
	 ContinueLoop
  EndIf

  WEnd


  EndFunc

