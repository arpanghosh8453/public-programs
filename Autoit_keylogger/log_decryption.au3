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
