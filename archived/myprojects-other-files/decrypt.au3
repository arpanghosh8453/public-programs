#include <MsgBoxConstants.au3>
;#include <Array.au3>
#include <File.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>

Local $f = FileOpenDialog("", @WindowsDir & "\", "All (*.*)")
Local $d = FileSaveDialog("", @WindowsDir & "\", "All (*.*)")
$k = Inputbox("Key","Enter the key number to recover:","1")
Example()

Func Example()
   fileopen($f)
   $a = fileread($f)
   fileclose($f)

    Local $aArray = StringToASCIIArray($a)
	$b =UBound($aArray)-1
for $i = 0 To $b Step 1
   $aArray[$i] = $aArray[$i]-$k
   Next
;_ArrayDisplay($aArray)
	Local $sString = StringFromASCIIArray($aArray)

;_FileCreate ($d)
FileOpen($d)
FileWrite($d,$sString)
FileClose($d)
Exit


EndFunc