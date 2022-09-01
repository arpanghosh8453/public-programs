#include <ComboConstants.au3>
#include <Crypt.au3>
#include <GUIConstantsEx.au3>
#include <MsgBoxConstants.au3>
#include <StringConstants.au3>
#include <GuiEdit.au3>
#include <ButtonConstants.au3>
#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Checker", 613, 431, 192, 132)

GUISetFont(20, 800, 0, "Arial Narrow")
$Input1 = GUICtrlCreateInput("", 176, 96, 305, 48)
;_GUICtrlEdit_SetPasswordChar ($Input1,"$")
GUICtrlSetColor(-1, 0x008000)
$Label1 = GUICtrlCreateLabel("Agent ID", 32, 96, 118, 44)
GUICtrlSetColor(-1, 0x800000)
$Label2 = GUICtrlCreateLabel("Password", 32, 224, 133, 44)
GUICtrlSetColor(-1, 0x800080)
$Input2 = GUICtrlCreateInput("", 176, 216, 313, 48)
_GUICtrlEdit_SetPasswordChar ($Input2,"*")
GUICtrlSetFont(-1, 24, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0xFF0000)
$Button1 = GUICtrlCreateButton("Log In", 192, 312, 209, 89)
GUICtrlSetFont(-1, 24, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0x00FF00)
$Label3 = GUICtrlCreateLabel("Verifier", 256, 16, 99, 44)
GUICtrlSetColor(-1, 0x000080)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 case $Button1
			login()


	EndSwitch
 WEnd

 func login()
	$pass = "jfmamjjasond"
     $id = "Arpan Ghosh"
	$p = GUICtrlRead($Input2)
    $i = GUICtrlRead($Input1)
	if $p == $pass and $i == $id Then
	   GUIDelete($Form1)
	   ProgressOn("Progress starter", "Speed status : Very Fast", "0%")
    For $i = 0 To 100 Step 5
        Sleep(100)
        ProgressSet($i, $i & "%")
		if $i == 50 Then
		   ProgressSet(50, "50%Done", "Almost Complete")
	       Sleep(100)
		 EndIf
   Next
	ProgressSet(100, "100% Done", "Ready.....Please Wait")
	Sleep(2000)
    ProgressOff()
	   go()
   Else
	   Msgbox(16,"Error","Agent Not Detected",2)
	   Exit

	EndIf

 EndFunc

Func go()

    Local $iAlgorithm = $CALG_RC4

    Local $hGUI = GUICreate("File Encrypter",613, 435, 192, 132)
    Local $idSourceInput = GUICtrlCreateInput("",48, 48, 257, 50)
	GUICtrlSetFont(-1, 14, 800, 0, "Arial")
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0xB9D1EA)
    Local $idSourceBrowse = GUICtrlCreateButton("Find File",344, 40, 169, 57)
	GUICtrlSetFont(-1, 14, 800, 0, "@Adobe Gothic Std B")
GUICtrlSetColor(-1, 0xFFFF00)
GUICtrlSetBkColor(-1, 0x808000)

	$Label2 = GUICtrlCreateLabel("Source",112, 0, 108, 47)
GUICtrlSetFont(-1, 22, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x000080)
GUICtrlSetBkColor(-1, 0x00FFFF)
$Label3 = GUICtrlCreateLabel("Destination",96, 96, 156, 47)
GUICtrlSetFont(-1, 22, 400, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0x00FFFF)

    Local $idDestinationInput = GUICtrlCreateInput("", 40, 144, 265, 50)
	GUICtrlSetFont(-1, 14, 800, 0, "Arial")
GUICtrlSetColor(-1, 0xFF0000)
GUICtrlSetBkColor(-1, 0xB9D1EA)
    Local $idDestinationBrowse =  GUICtrlCreateButton("Create File", 344, 144, 185, 65)
GUICtrlSetFont(-1, 14, 800, 0, "@Adobe Gothic Std B")
GUICtrlSetColor(-1, 0xFFFF00)
GUICtrlSetBkColor(-1, 0x808000)



    GUICtrlCreateLabel("Password:",24, 256, 173, 68)
	GUICtrlSetFont(-1, 26, 800, 0, "Arial Narrow")
	GUICtrlSetBkColor(-1, 0x99B4D1)
    Local $idPasswordInput = GUICtrlCreateInput("",224, 264, 297, 47)
	_GUICtrlEdit_SetPasswordChar ($idPasswordInput,"*")

	GUICtrlSetFont(-1, 22, 400, 0,"Arial")
GUICtrlSetColor(-1, 0x000080)
GUICtrlSetBkColor(-1, 0xFFFF00)


    Local $idCombo = GUICtrlCreateCombo("",48, 352, 177, 50, $CBS_DROPDOWNLIST)
	GUICtrlSetFont(-1, 14, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x008000)
GUICtrlSetBkColor(-1, 0xFF00FF)
    GUICtrlSetData($idCombo, "3DES|AES (128bit)|AES (192bit)|AES (256bit)|DES|RC2|RC4", "RC4")
    Local $idEncrypt =GUICtrlCreateButton("Encrypt", 288, 344, 153, 65)
	GUICtrlSetFont(-1, 24, 800, 0, "Arial Narrow")
GUICtrlSetColor(-1, 0x000080)
GUICtrlSetBkColor(-1, 0x00FF00)
    GUISetState(@SW_SHOW, $hGUI)

    Local $sDestinationRead = "", $sFilePath = "", $sPasswordRead = "", $sSourceRead = ""
    While 1
        Switch GUIGetMsg()
            Case $GUI_EVENT_CLOSE
                ExitLoop

            Case $idSourceBrowse
                $sFilePath = FileOpenDialog("Select a file to encrypt.", "", "All files (*.*)") ; Select a file to encrypt.
                If @error Then
                    ContinueLoop
                EndIf
                GUICtrlSetData($idSourceInput, $sFilePath) ; Set the inputbox with the filepath.

            Case $idDestinationBrowse
                $sFilePath = FileSaveDialog("Save the file as ...", "", "All files (*.*)") ; Select a file to save the encrypted data to.
                If @error Then
                    ContinueLoop
                EndIf
                GUICtrlSetData($idDestinationInput, $sFilePath) ; Set the inputbox with the filepath.

            Case $idCombo ; Check when the combobox is selected and retrieve the correct algorithm.
                Switch GUICtrlRead($idCombo) ; Read the combobox selection.
                    Case "3DES"
                        $iAlgorithm = $CALG_3DES

                    Case "AES (128bit)"
                        $iAlgorithm = $CALG_AES_128

                    Case "AES (192bit)"
                        $iAlgorithm = $CALG_AES_192

                    Case "AES (256bit)"
                        $iAlgorithm = $CALG_AES_256

                    Case "DES"
                        $iAlgorithm = $CALG_DES

                    Case "RC2"
                        $iAlgorithm = $CALG_RC2

                    Case "RC4"
                        $iAlgorithm = $CALG_RC4

                EndSwitch

            Case $idEncrypt
                $sSourceRead = GUICtrlRead($idSourceInput) ; Read the source filepath input.
                $sDestinationRead = GUICtrlRead($idDestinationInput) ; Read the destination filepath input.
                $sPasswordRead = GUICtrlRead($idPasswordInput) ; Read the password input.
                If StringStripWS($sSourceRead, $STR_STRIPALL) <> "" And StringStripWS($sDestinationRead, $STR_STRIPALL) <> "" And StringStripWS($sPasswordRead, $STR_STRIPALL) <> "" And FileExists($sSourceRead) Then ; Check there is a file available to encrypt and a password has been set.
                    If _Crypt_EncryptFile($sSourceRead, $sDestinationRead, $sPasswordRead, $iAlgorithm) Then ; Encrypt the file.
                        MsgBox($MB_SYSTEMMODAL, "Success", "Operation succeeded.")
                    Else
                        Switch @error
                            Case 1
                                MsgBox($MB_SYSTEMMODAL, "Error", "Failed to create the key.")
                            Case 2
                                MsgBox($MB_SYSTEMMODAL, "Error", "Couldn't open the source file.")
                            Case 3
                                MsgBox($MB_SYSTEMMODAL, "Error", "Couldn't open the destination file.")
                            Case 4 Or 5
                                MsgBox($MB_SYSTEMMODAL, "Error", "Encryption error.")
                        EndSwitch
                    EndIf
                Else
                    MsgBox($MB_SYSTEMMODAL, "Error", "Please ensure the relevant information has been entered correctly.")
                EndIf
        EndSwitch
    WEnd

    GUIDelete($hGUI) ; Delete the previous GUI and all controls.
EndFunc   ;==>Example
