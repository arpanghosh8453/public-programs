#include <File.au3>
#include <MsgBoxConstants.au3>
;#include <Array.au3>
#include <File.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>



$i = Inputbox("number","Enter The number")
$c = Inputbox("count","Enter the last number")
Local $f = FilesaveDialog("", @WindowsDir & "\", "All (*.*)")
$c = $c + 1

Sleep(1000)
$n = 1
While($c>$n)
    fileopen($f)

   $r = ($i * $n)
   filewrite($f,$i & " X " & $n & " = " & $r & @CRLF)

   $n = $n+1
WEnd

exit