#include <ButtonConstants.au3>
#include <ComboConstants.au3>
#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#include <GuiButton.au3>
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Calculator", 765, 532, 171, 135)
GUISetBkColor(0xC0DCC0)
$Label1 = GUICtrlCreateLabel("calculator", 272, 24, 207, 53)
GUICtrlSetFont(-1, 26, 800, 2, "Arial")
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0x00FFFF)
$Input1 = GUICtrlCreateInput("", 16, 128, 257, 100)
GUICtrlSetFont(-1, 36, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x808000)
GUICtrlSetBkColor(-1, 0xD7E4F2)

$Label3 = GUICtrlCreateLabel("RESULT",48, 288, 141, 44)
GUICtrlSetFont(-1, 20, 800, 0, "Arial")
GUICtrlSetColor(-1, 0x008000)
GUICtrlSetBkColor(-1, 0xBFCDDB)
$Combo1 = GUICtrlCreateCombo("Add", 296, 152, 161, 300, BitOR($CBS_DROPDOWN,$CBS_AUTOHSCROLL))
GUICtrlSetData($Combo1, "Substract|Multiply|Divide|Percentage|Modulus", "Add")
GUICtrlSetFont(-1, 18, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x800080)
GUICtrlSetBkColor(-1, 0xA6CAF0)
$CALCULATE = GUICtrlCreateButton("CALCULATE",  56, 416, 465, 89)
GUICtrlSetFont(-1, 26, 800, 4, "@Kozuka Gothic Pr6N M")
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0x00FF00)
$Button1 = GUICtrlCreateButton("Refresh",  592, 416, 161, 89)
GUICtrlSetFont(-1, 22, 800, 4, "Arial")
GUICtrlSetColor(-1, 0x008000)
GUICtrlSetBkColor(-1, 0xB9D1EA)


$Label4 = GUICtrlCreateLabel("", 216, 256,500, 105)
GUICtrlSetFont(-1, 30, 800, 2, "Arial")
GUICtrlSetColor(-1, 0xFF00FF)
GUICtrlSetBkColor(-1, 0x00FFFF)
$Input2 = GUICtrlCreateInput("", 480, 128, 265, 100)
GUICtrlSetFont(-1, 36, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x808000)
GUICtrlSetBkColor(-1, 0xD7E4F2)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###
_GUICtrlButton_Enable ($Button1,False)
While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 case $CALCULATE
			count()
		 case $Button1
			refresh()


	EndSwitch
 WEnd
 func count()
	$f = GUICtrlRead($Input1)
	$s = GUICtrlRead($Input2)
	$c  = GUICtrlRead($Combo1)
	Switch $c
	   case "Add"
          $r = $f + $s
	   case "Substract"
		  $r = $f - $s
	   Case "Multiply"
		  $r = $f * $s
	   Case "Modulus"
		  $r = Mod($f,$s)
	   Case "Percentage"
		  $r = ($s * 100)/$f
	   Case "Divide"
		  $r = $f/$s
	   Case Else
		  Msgbox(16,"Wrong","Wrong Choice!!")
	   EndSwitch
	   GUICtrlSetData($Label4,$r)
	   _GUICtrlButton_Enable ($Button1,True)
	    _GUICtrlButton_Enable ($CALCULATE,False)

	EndFunc
func refresh()
   GUICtrlSetData($Input1,"")
   GUICtrlSetData($Input2,"")
   GUICtrlSetData($Label4,"")
   _GUICtrlButton_Enable ($Button1,False)
   _GUICtrlButton_Enable ($CALCULATE,True)
EndFunc

