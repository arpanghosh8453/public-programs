Public Class Game
    Public level As Integer = 1
    Public score As Integer = 0
    Public played As Integer = 0
    Public delay As Integer = (level * (3 / 2)) + 2
    Public answer As String = ""

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Try 
            level = ComboBox1.Text
            delay = (level * (3 / 2)) + 2
            answer = randstring(level)
            Label1.Text = "Remember : " & answer
            ComboBox1.Enabled = False
            Button1.Enabled = False
            Timer1.Start()
        Catch
            ComboBox1.Text = 1
            MsgBox("Please Enter A Valid Level Number And Retry!! ")
        End Try

    End Sub
    Private Function randstring(level) As String
        Dim mainstring As String = "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+=-{}[]:;'<>?,./~"
        Dim substring As String = mainstring.Substring(0, level * 10)
        Dim randnum As New Random
        Dim looplevel As Integer
        Dim final As String = ""
        For looplevel = 0 To (level + 3)
            final = final + substring.Substring(randnum.Next(0, substring.Length - 1), 1)
        Next
        Return final
    End Function

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Timer1.Stop()
        TextBox1.Enabled = False
        ComboBox1.Enabled = True

        If TextBox1.Text = answer Then
            Label1.Text = "Congratulations to you !! "
            MsgBox("Great Memory !! You are correct!! Try the next level !")
            If level < 9 Then
                ComboBox1.Text = level + 1
            End If
            score = score + level
            Label6.Text = score
            Label7.Text = Label7.Text + 1
        Else
            Label1.Text = "Correct Answer was : " & answer
            MsgBox("Sorry!! You are Wrong !! Try Again !")
            Label7.Text = Label7.Text + 1
        End If
        TextBox1.Text = ""
        Button1.Enabled = True
        Button2.Enabled = False
        Label1.Text = "Click 'SHOW' To Replay The Game"
        Label2.Text = "Entry Disabled!"
    End Sub

    Private Sub Timer1_Tick(sender As System.Object, e As System.EventArgs) Handles Timer1.Tick
        delay -= 1
        If delay >= 0 Then
            Label2.Text = "Time Remaining : " & delay & " Seconds"
        ElseIf delay >= -5 Then
            Label2.Text = "Wait And Remind For " & 6 + delay & " Seconds more!!"
        End If
        If delay = 0 Then
            Label1.Text = "Time is up!!"
        End If
        If delay = -6 Then
            Label2.Text = "Enter the value now ... "
            TextBox1.Enabled = True
            Button2.Enabled = True
        End If
    End Sub
End Class
