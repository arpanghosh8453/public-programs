Public Class Timer

    Public totalTime As Double = 0
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        totaltime = ((hourbox.Value * 3600) + (minutebox.Value * 60) + (secondbox.Value)) * 100
        Button1.Enabled = False
        Button2.Enabled = True
        hourbox.Enabled = False
        minutebox.Enabled = False
        secondbox.Enabled = False
        Timer1.Start()
        Timer2.Stop()
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Button1.Enabled = True
        Timer1.Stop()
    End Sub

    Private Sub Timer1_Tick(sender As System.Object, e As System.EventArgs) Handles Timer1.Tick
        Dim show As Boolean = True
        Dim hour As Double
        Dim minute As Double
        Dim second As Double
        Dim milisecond As Long

        If totalTime = -1 Then
            Label4.Text = "TIME IS UP !! "
            Timer1.Stop()
            Timer2.Start()
        ElseIf totalTime >= 0 Then
            totalTime = totalTime - 1
            milisecond = totalTime Mod 6000
            second = milisecond / 100
            minute = ((totalTime - (totalTime Mod 6000)) / 6000) Mod 60
            hour = ((totalTime - (totalTime Mod 6000)) / 6000) / 60
            If hour < 1 Then
                hour = 0
            End If
            If minute < 0 Then
                minute = 0
            End If
            If second < 0 Then
                second = 0.0
            End If
            hourbox.Value = hour
            minutebox.Value = minute
            secondbox.Value = second
        Else
            Timer1.Stop()
        End If



        
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        Timer1.Stop()
        Timer2.Stop()
        hourbox.Value = 0
        minutebox.Value = 0
        secondbox.Value = 0.0
        hourbox.Enabled = True
        minutebox.Enabled = True
        secondbox.Enabled = True
        Button1.Enabled = True
        Button2.Enabled = False
        Label4.Text = "TIMER"
    End Sub

    Private Sub Timer2_Tick(sender As System.Object, e As System.EventArgs) Handles Timer2.Tick
        Dim newvalue As String = "Pause"
    End Sub
End Class
