#include <Crypt.au3>
#include <FileConstants.au3>
#include <file.au3>
#include <File.au3>
#include <Array.au3>

Func isdir($sFilePath)
    ;Get the attribute string and check if it contains the letter "D".
    If StringInStr(FileGetAttrib($sFilePath), "D") = 0 Then
       Return False
    Else
        Return True
    EndIf
EndFunc

Local $szDrive = "", $szDir = "", $szFName = "", $szExt = ""
Local $Infilepath = InputBox("Filename or foldername","Enter the full filepath or folderpath to decrypt it",@scriptdir)
$is_dir = isdir($Infilepath )
if $is_dir Then
   $FileList = _FileListToArray($Infilepath)
   If @error = 1 Then
	  MsgBox(0, "", "No Files\Folders Found.")
	  Exit
   EndIf
   DirCreate($Infilepath&"\Decrypted")
Else
   Local $FileList[1] = [$Infilepath]
EndIf

Local $password = InputBox("Password","Enter the Password to decrypt the file","Password","*")

For $Encryptedfile In $FileList
   if $is_dir = True Then
	  $Encrypted = $Infilepath&"\"&$Encryptedfile
   Else
	  $Encrypted  = $Encryptedfile
   EndIf
   _PathSplit($Encrypted, $szDrive, $szDir, $szFName, $szExt)
   if $is_dir = True Then
	  $szDir = $szDir&"Decrypted\"
   EndIf
   if $szExt = ".rcd" Then
	  Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.htm"
   ElseIf $szExt = ".pic" Then
	  Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.jpg"
   Elseif  $szExt = ".tsk" Then
	  Local $Decrypted = $szDrive & $szDir & $szFName & "_decrypted.txt"
   Else
	  Local $Decrypted = ""
   EndIf
   ;CODE FOR Decryption starts---------------------------------------------------------------------------------

   if $szExt = ".rcd" Then
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
   Elseif $Decrypted <> "" Then
	   _Crypt_DecryptFile($Encrypted, $Decrypted, $password, $CALG_AES_256)
   EndIf
   If $Decrypted <> "" and $is_dir = False Then
   MsgBox (64,"Confirmation", "Encrypted data have been successfully decrypted and saved in " & $Decrypted)
   EndIf
Next
If $is_dir = True Then
   MsgBox (64,"Confirmation", "Encrypted data have been successfully decrypted")
   EndIf

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