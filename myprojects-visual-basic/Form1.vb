Public Class Form1
    Public teamname As String = "X"
    Public ifwins As Boolean = False
    Public partner As String = "Computer"
    Public frozen As Boolean = False

    Public Sub freeze()
        teamname = "X"
        Button1.Enabled = False
        Button2.Enabled = False
        Button3.Enabled = False
        Button4.Enabled = False
        Button5.Enabled = False
        Button6.Enabled = False
        Button7.Enabled = False
        Button8.Enabled = False
        Button9.Enabled = False
        frozen = True
    End Sub
    Public Sub teamchange()
        If teamname = "X" Then
            teamname = "O"
        Else
            teamname = "X"
        End If
        Label1.Text = "Turn Of Team : '" & teamname & "'"
    End Sub
    Public Function whowins() As Boolean
        If (Button1.Text = Button2.Text) And (Button2.Text = Button3.Text) Then
            If Button1.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button1.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If
        End If
        If (Button4.Text = Button5.Text) And (Button4.Text = Button6.Text) Then
            If Button4.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button4.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If


        End If
        If (Button7.Text = Button8.Text) And (Button8.Text = Button9.Text) Then
            If Button7.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button7.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If
        End If
        If (Button1.Text = Button4.Text) And (Button4.Text = Button7.Text) Then
            If Button1.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button1.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If

        End If
        If (Button2.Text = Button5.Text) And (Button5.Text = Button8.Text) Then
            If Button2.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button2.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If

        End If
        If (Button3.Text = Button6.Text) And (Button6.Text = Button9.Text) Then
            If Button3.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button3.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If

        End If
        If (Button1.Text = Button5.Text) And (Button5.Text = Button9.Text) Then
            If Button1.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button1.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If

        End If
        If (Button3.Text = Button5.Text) And (Button5.Text = Button7.Text) Then
            If Button3.Text = "X" Then
                Label1.Text = "Team 'X' Is The Winner !! "
                Label5.Text = Label5.Text + 1
                freeze()
                Return True
            ElseIf Button3.Text = "O" Then
                Label1.Text = "Team 'O' Is The Winner !! "
                Label6.Text = Label6.Text + 1
                freeze()
                Return True
            End If
        End If
        Return False
    End Function
    Public Sub isdraw()
        If (Button1.Text = "?" Or Button2.Text = "?") Or (Button3.Text = "?" Or Button4.Text = "?") Then
            Dim none As String = Nothing
        ElseIf (Button5.Text = "?" Or Button6.Text = "?") Or (Button7.Text = "?" Or Button8.Text = "?") Then
            Dim none As String = Nothing
        ElseIf Button9.Text = "?" Then
            Dim none As String = Nothing
        Else
            Label1.Text = "The Game Is Draw !! "
            Label7.Text = Label7.Text + 1
            freeze()
        End If
    End Sub
    Public Function isincomplete() As Boolean
        If frozen = True Then
            Return False
        ElseIf Button1.Text <> "?" Then
            Return True
        ElseIf Button2.Text <> "?" Then
            Return True
        ElseIf Button3.Text <> "?" Then
            Return True
        ElseIf Button4.Text <> "?" Then
            Return True
        ElseIf Button5.Text <> "?" Then
            Return True
        ElseIf Button6.Text <> "?" Then
            Return True
        ElseIf Button7.Text <> "?" Then
            Return True
        ElseIf Button8.Text <> "?" Then
            Return True
        ElseIf Button9.Text <> "?" Then
            Return True
        Else
            Return False
        End If
    End Function
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Button1.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button1.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If

    End Sub
    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Button2.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button2.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        Button3.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button3.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button4_Click(sender As System.Object, e As System.EventArgs) Handles Button4.Click
        Button4.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button4.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button5_Click(sender As System.Object, e As System.EventArgs) Handles Button5.Click
        Button5.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button5.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button6_Click(sender As System.Object, e As System.EventArgs) Handles Button6.Click
        Button6.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button6.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button7_Click(sender As System.Object, e As System.EventArgs) Handles Button7.Click
        Button7.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button7.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub

    Private Sub Button8_Click(sender As System.Object, e As System.EventArgs) Handles Button8.Click
        Button8.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button8.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub
    Private Sub Button9_Click(sender As System.Object, e As System.EventArgs) Handles Button9.Click
        Button9.Text = teamname
        teamchange()
        ifwins = whowins()
        If ifwins = False Then
            isdraw()
        End If
        Button9.Enabled = False
        If partner = "Computer" Then
            compturn()
        End If
    End Sub
    Public Sub compturn()
        If teamname = "X" Then
            Dim abc As String = Nothing
        Else
            If (Button1.Text = Button2.Text) And (Button1.Text <> "?" And Button3.Text = "?") Then
                Button3.PerformClick()
            ElseIf (Button1.Text = Button3.Text) And (Button1.Text <> "?" And Button2.Text = "?") Then
                Button2.PerformClick()
            ElseIf (Button2.Text = Button3.Text) And (Button2.Text <> "?" And Button1.Text = "?") Then
                Button1.PerformClick()
            ElseIf (Button4.Text = Button5.Text) And (Button4.Text <> "?" And Button6.Text = "?") Then
                Button6.PerformClick()
            ElseIf (Button5.Text = Button6.Text) And (Button5.Text <> "?" And Button4.Text = "?") Then
                Button4.PerformClick()
            ElseIf (Button4.Text = Button6.Text) And (Button4.Text <> "?" And Button5.Text = "?") Then
                Button5.PerformClick()
            ElseIf (Button7.Text = Button8.Text) And (Button7.Text <> "?" And Button9.Text = "?") Then
                Button9.PerformClick()
            ElseIf (Button8.Text = Button9.Text) And (Button8.Text <> "?" And Button7.Text = "?") Then
                Button7.PerformClick()
            ElseIf (Button7.Text = Button9.Text) And (Button7.Text <> "?" And Button8.Text = "?") Then
                Button8.PerformClick()
            ElseIf (Button1.Text = Button4.Text) And (Button4.Text <> "?" And Button7.Text = "?") Then
                Button7.PerformClick()
            ElseIf (Button1.Text = Button7.Text) And (Button1.Text <> "?" And Button4.Text = "?") Then
                Button4.PerformClick()
            ElseIf (Button4.Text = Button7.Text) And (Button4.Text <> "?" And Button1.Text = "?") Then
                Button1.PerformClick()
            ElseIf (Button2.Text = Button5.Text) And (Button2.Text <> "?" And Button8.Text = "?") Then
                Button8.PerformClick()
            ElseIf (Button2.Text = Button8.Text) And (Button2.Text <> "?" And Button5.Text = "?") Then
                Button5.PerformClick()
            ElseIf (Button5.Text = Button8.Text) And (Button5.Text <> "?" And Button2.Text = "?") Then
                Button2.PerformClick()
            ElseIf (Button3.Text = Button6.Text) And (Button3.Text <> "?" And Button9.Text = "?") Then
                Button9.PerformClick()
            ElseIf (Button3.Text = Button9.Text) And (Button3.Text <> "?" And Button6.Text = "?") Then
                Button6.PerformClick()
            ElseIf (Button6.Text = Button9.Text) And (Button6.Text <> "?" And Button3.Text = "?") Then
                Button3.PerformClick()
            ElseIf (Button1.Text = Button5.Text) And (Button1.Text <> "?" And Button9.Text = "?") Then
                Button9.PerformClick()
            ElseIf (Button1.Text = Button9.Text) And (Button1.Text <> "?" And Button5.Text = "?") Then
                Button5.PerformClick()
            ElseIf (Button5.Text = Button9.Text) And (Button5.Text <> "?" And Button1.Text = "?") Then
                Button1.PerformClick()
            ElseIf (Button3.Text = Button5.Text) And (Button3.Text <> "?" And Button7.Text = "?") Then
                Button7.PerformClick()
            ElseIf (Button3.Text = Button7.Text) And (Button3.Text <> "?" And Button5.Text = "?") Then
                Button5.PerformClick()
            ElseIf (Button5.Text = Button7.Text) And (Button5.Text <> "?" And Button3.Text = "?") Then
                Button3.PerformClick()
            Else
                Dim randnum As Integer = 1
                Dim randgen As New System.Random
                Dim notgiven As Boolean = True
                While notgiven = True
                    randnum = randgen.Next(1, 10)
                    If randnum = 1 And Button1.Text = "?" Then
                        Button1.PerformClick()
                        notgiven = False
                    ElseIf randnum = 2 And Button2.Text = "?" Then
                        Button2.PerformClick()
                        notgiven = False
                    ElseIf randnum = 3 And Button3.Text = "?" Then
                        Button3.PerformClick()
                        notgiven = False
                    ElseIf randnum = 4 And Button4.Text = "?" Then
                        Button4.PerformClick()
                        notgiven = False
                    ElseIf randnum = 5 And Button5.Text = "?" Then
                        Button5.PerformClick()
                        notgiven = False
                    ElseIf randnum = 6 And Button6.Text = "?" Then
                        Button6.PerformClick()
                        notgiven = False
                    ElseIf randnum = 7 And Button7.Text = "?" Then
                        Button7.PerformClick()
                        notgiven = False
                    ElseIf randnum = 8 And Button8.Text = "?" Then
                        Button8.PerformClick()
                        notgiven = False
                    ElseIf randnum = 9 And Button9.Text = "?" Then
                        Button9.PerformClick()
                        notgiven = False
                    End If
                End While
            End If
        End If
    End Sub


    Private Sub Button10_Click(sender As System.Object, e As System.EventArgs) Handles Button10.Click
        If isincomplete() = True Then
            Label9.Text = Label9.Text + 1
        End If

        Button1.Text = "?"
        Button1.Enabled = True
        Button2.Text = "?"
        Button2.Enabled = True
        Button3.Text = "?"
        Button3.Enabled = True
        Button4.Text = "?"
        Button4.Enabled = True
        Button5.Text = "?"
        Button5.Enabled = True
        Button6.Text = "?"
        Button6.Enabled = True
        Button7.Text = "?"
        Button7.Enabled = True
        Button8.Text = "?"
        Button8.Enabled = True
        Button9.Text = "?"
        Button9.Enabled = True
        teamname = "X"
        Label1.Text = "Restarted : Turn Of Team 'X'"
        If RadioButton1.Checked = True Then
            partner = "Computer"
        Else
            partner = "Human"
        End If
        frozen = False
    End Sub
End Class
