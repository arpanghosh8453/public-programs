#include-once

; #INDEX# ========================================================================================================================
; Title .........: Math root
; AutoIt Version : 3.3.0.0 / 3.3.1.1
; Language ......: English
; Description ...: Deals with the nth root, including negative numbers.
; Author(s) .....: MDiesel
; ================================================================================================================================

; #FUNCTION# =====================================================================================================================
; Name...........: _RealRoot
; Description ...: Finds the real nth root of a number, including negatives.
; Syntax.........: _RealRoot($fNum, $nExp = 3)
; Parameters ....: $fNum       - The Number
;                  $nExp       - The root.
; Return values .: On Success: = Returns the result.
;                  On Failure: = Sets @Error and returns 0, which can be a valid responce, so check @Error first.
;                  @ERROR:     = 0 = No error.
;                                1 - Result is an imaginay number
; Author ........: MDiesel
; Remarks .......:
; Example .......: ConsoleWrite("Normal = " & -27^(1/3) & @CRLF & "_RealRoot  = " & _RealRoot(-27, 3))
; ================================================================================================================================
$a = _RealRoot(65536,8)
MsgBox(0,0,$a)

Func _RealRoot($fNum, $nExp = 3)
   Local $bNeg = False, $fRet = 0
   If $nExp < 0 Then Return SetError (1, 0, $fNum)

   If $fNum < 0 Then ; is negative
      If Mod($nExp, 2) Then ; nExp is odd, so negative IS possible.
         $bNeg = True
         $fNum *= -1
      Else
         Return SetError(16, "Error", $fNum & "i") ; Imaginary number.
      EndIf
   EndIf

   $fRet = $fNum ^ (1 / $nExp)
   If $bNeg Then $fRet *= -1
   Return $fRet
EndFunc ; ==> _RealRoot