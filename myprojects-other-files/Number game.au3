hotkeyset("^m","start")
$pass = "Arpan"
$input = Inputbox("pass","Enter the password","","$")
If $input = $pass Then
   msgbox(64,"Correct","Thank You!!",2)
Else
   Msgbox(16,"Wrong","OUT of the game!!",2)
   Exit
EndIf
sleep(500)
Msgbox(64,"information","The computer guessed number will contain digits same as the level number and will not contain any repeated digits")
Sleep(500)
$r = Inputbox("Level","Enter the digit cum level number")
$chance = Inputbox("chance","Enter the guess chance")
$c = 1
$n = Random(1,9,1)
If $r<10 and $r>0 Then
   while($r>$c)
	  $g = random(0,9,1)
	  $a = $n
	  $m = 0
	  While($a>0)
		 $x = Mod($a,10)
		 $a = (($a-$x)/10)
		 If $g = $x Then
			if $m = 0 Then
			   $g = 9
			   $m = 1
			Else
			   $g = ($g-1)
			EndIf
			$a = $n
		 Else
			$g = $g
		 EndIf
	  WEnd
	  $n = (($n*10)+$g)
	  $c = ($c+1)
   WEnd
Else
   msgbox(16,"Error","Level name is incorrect")
   Exit
EndIf
Msgbox(64,"Information","Press 'ctrl + m' to see the number and exit")

Func start()
   msgbox(64,"Number",$n)
   Exit
EndFunc
Run("notepad.exe")
Sleep(500)
$count = 0
While($chance>$count)
   $i = Inputbox("Number","Enter your guessed number")
   $count = $count + 1
   If $n = $i Then
	  Send($n)
	  Send(" (YOU WIN!!) ")
	  sleep(100)
	  Msgbox(64,$count,"Correct Guess!!")
	  Exit
   Else
	  $i = $i
   EndIf
   $b = 0
   $f = $i
   While($f>0)
	  $k = Mod($f,10)
	  $f = (($f-$k)/10)
	  $b = $b + 1
   WEnd
   if $b = $r Then
	  $r = $r
   Else
	  Msgbox(16,"Error","Wrong digited number")
	  Exit
   EndIf
   $m = $i
    While($m>0)
	   $a = Mod($m,10)
	   $m = (($m-$a)/10)
	   $s = $m
	   While($s>0)
		  $y = Mod($s,10)
		  $s = (($s-$y)/10)
		  If $a = $y Then
			 Msgbox(16,"Error","All numbers are not different")
			 Exit
		  Else
			 $y = $y
		  EndIf
	   WEnd
	WEnd

   $v = 0
   $true = 0
   $f = 0
   $t = $n
   While($t>0)
	  $p = Mod($t,10)
	  $t = (($t-$p)/10)
	  $v = ($v+1)
	  $t1 = $i
	  $v1 = 0
	  While($t1>0)
		 $p1 = Mod($t1,10)
		 $t1 = (($t1-$p1)/10)
		 $v1 = ($v1 + 1)
		 If $p = $p1 And $v = $v1 Then
			$true = ($true + 1)
			ExitLoop
		 ElseIf $p = $p1 Then
			$f = ($f + 1)
			ExitLoop
		 Else
			$r = $r
		 EndIf
	  WEnd
   WEnd
   WinActivate("Untitled Notepad")
   send(" ")
   Send($count)
   Send(") ")
   $nf = ($r - ($true + $f))
   Send($i)
   Send(" = ")
   Send(" ( Correctplaces = ")
   Send($true)
   Send(" ) , ( Wrongplaces = ")
   Send($f)
   Send(" ) , ( Errorguess = ")
   Send($nf)
   Send(" )")
   Send("{ENTER}")
WEnd
send("Correct answer is : ")
Send($n)
Send("{ENTER}")
Send("( You LOST!! )")
sleep(100)
Msgbox(16,"Sorry!","The chance is over!!",2)
Msgbox(16,"Status","You have lost the game!!",2)
Exit





