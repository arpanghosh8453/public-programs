while(1)
   ProcessWait("vlc.exe")
   Send ("{VOLUME_MUTE}")
   sleep(random(5000,12000,1))
WEnd

