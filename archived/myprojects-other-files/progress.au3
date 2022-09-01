ProgressOn("Progress Meter", "Increments every second", "0 percent")
For $i = 0 To 100 Step 30
    Sleep(1000)
    ProgressSet($i, $i & " percent")
Next
ProgressSet(100, "Done", "Complete")
Sleep(2000)
ProgressOff()


