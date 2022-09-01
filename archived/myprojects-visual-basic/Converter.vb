Public Class Form1
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click

        Try
            Dim input As Double = TextBox1.Text
            Dim result As Double = Nothing
            If RadioButton1.Checked = True Then
                result = ((input * 9) + 160) / 5
                Label2.Text = "Centigrade : " & input
                Label3.Text = "Fahrenheit  : " & result
            ElseIf RadioButton2.Checked = True Then
                result = ((5 * input) - 160) / 9
                Label2.Text = "Fahrenheit : " & input
                Label3.Text = "Centigrade : " & result
            ElseIf RadioButton3.Checked = True Then
                result = input + 273
                If result < 0 Then
                    Label2.Text = "Centigrade : " & input
                    Label3.Text = "Kelvin : " & "No Negative Value is Avilable !"
                Else
                    Label2.Text = "Centigrade : " & input
                    Label3.Text = "Kelvin : " & result
                End If
            ElseIf RadioButton4.Checked = True Then
                result = (((5 * input) - 160) / 9) + 273
                If result < 0 Then
                    Label2.Text = "Fahrenheit : " & input
                    Label3.Text = "Kelvin : " & "No Negative Value is Avilable ! "
                Else
                    Label2.Text = "Fahrenheit : " & input
                    Label3.Text = "Kelvin : " & result
                End If
            ElseIf RadioButton5.Checked = True Then
                result = (((input - 273) * 9) + 160) / 5
                If input < 0 Then
                    Label2.Text = "Kelvin : " & "No Negative Value is Avilable ! "
                    Label3.Text = "Fahrenheit  : " & "Calculation Failed !! "
                Else
                    Label2.Text = "Kelvin : " & input
                    Label3.Text = "Fahrenheit  : " & result
                End If
            ElseIf RadioButton6.Checked = True Then
                result = input - 273
                If input < 0 Then
                    Label2.Text = "Kelvin : " & "No Negative Value is Avilable ! "
                    Label3.Text = "Centigrade : " & "Calculation Failed !! "
                Else
                    Label2.Text = "Kelvin : " & input
                    Label3.Text = "Centigrade : " & result
                End If
            End If
        Catch ex As Exception
            MsgBox("Please Enter a Correct Value !! ")
            Button2.PerformClick()
        End Try

    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Label2.Text = "Enter a value And Click Convert"
        TextBox1.Text = ""
        Label3.Text = "Your Result Will Be Shown Here"
        RadioButton1.Checked = True
    End Sub
End Class