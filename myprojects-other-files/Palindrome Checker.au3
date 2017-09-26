#include <File.au3>
_FileCreate ("C:\Users\Hi\Desktop\new.txt")


$s = Inputbox("Number","Enter the number")
$i = Inputbox("steps","Enter the number of steps to check")
$sum = $s
$st = 0
While($st<$i)
   $n = $sum
   $r = 0
   While($n>0)
	  $a = Mod($n,10)
	  $n = (($N-$a)/10)
	  $r = (($r + $a)*10)
   WEnd

   FileOpen("C:\Users\Hi\Desktop\new.txt")
   filewrite("C:\Users\Hi\Desktop\new.txt",$r)
   filewrite("C:\Users\Hi\Desktop\new.txt",@CRLF)
   $r = ($r/10)
   If $sum = $r And $st>0 Then
	  $c=0
	  ExitLoop
   Else
	  $sum = ($sum+$r)
	  $c = 1
	  $st = $st + 1
   EndIf
WEnd
If $c = 1 Then
   Msgbox(16,"Incompleted","More steps Needed")
Else
   Msgbox(64,"Checked steps",$st)
   Msgbox(64,"Palindrome",$sum)
EndIf
Exit
