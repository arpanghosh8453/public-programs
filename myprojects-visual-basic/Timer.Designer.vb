<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Timer
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Timer))
        Me.hourbox = New System.Windows.Forms.NumericUpDown()
        Me.minutebox = New System.Windows.Forms.NumericUpDown()
        Me.secondbox = New System.Windows.Forms.NumericUpDown()
        Me.Timer1 = New System.Windows.Forms.Timer(Me.components)
        Me.Button1 = New System.Windows.Forms.Button()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.Button3 = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Timer2 = New System.Windows.Forms.Timer(Me.components)
        CType(Me.hourbox, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.minutebox, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.secondbox, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'hourbox
        '
        Me.hourbox.AutoSize = True
        Me.hourbox.BackColor = System.Drawing.Color.AntiqueWhite
        Me.hourbox.Font = New System.Drawing.Font("Microsoft Sans Serif", 36.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.hourbox.ForeColor = System.Drawing.Color.Brown
        Me.hourbox.Location = New System.Drawing.Point(25, 152)
        Me.hourbox.Maximum = New Decimal(New Integer() {24, 0, 0, 0})
        Me.hourbox.Name = "hourbox"
        Me.hourbox.Size = New System.Drawing.Size(129, 62)
        Me.hourbox.TabIndex = 0
        Me.hourbox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'minutebox
        '
        Me.minutebox.AutoSize = True
        Me.minutebox.BackColor = System.Drawing.Color.AntiqueWhite
        Me.minutebox.Font = New System.Drawing.Font("Microsoft Sans Serif", 36.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.minutebox.ForeColor = System.Drawing.Color.Brown
        Me.minutebox.Location = New System.Drawing.Point(182, 152)
        Me.minutebox.Maximum = New Decimal(New Integer() {59, 0, 0, 0})
        Me.minutebox.Name = "minutebox"
        Me.minutebox.Size = New System.Drawing.Size(126, 62)
        Me.minutebox.TabIndex = 1
        Me.minutebox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'secondbox
        '
        Me.secondbox.AutoSize = True
        Me.secondbox.BackColor = System.Drawing.Color.AntiqueWhite
        Me.secondbox.DecimalPlaces = 2
        Me.secondbox.Font = New System.Drawing.Font("Microsoft Sans Serif", 36.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.secondbox.ForeColor = System.Drawing.Color.Brown
        Me.secondbox.Location = New System.Drawing.Point(337, 152)
        Me.secondbox.Maximum = New Decimal(New Integer() {5999, 0, 0, 131072})
        Me.secondbox.Name = "secondbox"
        Me.secondbox.Size = New System.Drawing.Size(161, 62)
        Me.secondbox.TabIndex = 2
        Me.secondbox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        '
        'Timer1
        '
        Me.Timer1.Interval = 1
        '
        'Button1
        '
        Me.Button1.BackColor = System.Drawing.Color.LawnGreen
        Me.Button1.Font = New System.Drawing.Font("Arial Rounded MT Bold", 21.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Button1.ForeColor = System.Drawing.Color.DarkRed
        Me.Button1.Location = New System.Drawing.Point(18, 259)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(142, 57)
        Me.Button1.TabIndex = 3
        Me.Button1.Text = "Start"
        Me.Button1.UseVisualStyleBackColor = False
        '
        'Button2
        '
        Me.Button2.BackColor = System.Drawing.Color.Red
        Me.Button2.Enabled = False
        Me.Button2.Font = New System.Drawing.Font("Arial Rounded MT Bold", 21.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Button2.ForeColor = System.Drawing.Color.Gold
        Me.Button2.Location = New System.Drawing.Point(195, 260)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(141, 56)
        Me.Button2.TabIndex = 4
        Me.Button2.Text = "Pause"
        Me.Button2.UseVisualStyleBackColor = False
        '
        'Button3
        '
        Me.Button3.BackColor = System.Drawing.Color.DarkOrange
        Me.Button3.Font = New System.Drawing.Font("Arial Rounded MT Bold", 21.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Button3.ForeColor = System.Drawing.Color.DarkBlue
        Me.Button3.Location = New System.Drawing.Point(368, 260)
        Me.Button3.Name = "Button3"
        Me.Button3.Size = New System.Drawing.Size(138, 55)
        Me.Button3.TabIndex = 5
        Me.Button3.Text = "Reset"
        Me.Button3.UseVisualStyleBackColor = False
        '
        'Label1
        '
        Me.Label1.BackColor = System.Drawing.Color.DarkBlue
        Me.Label1.Font = New System.Drawing.Font("Microsoft Sans Serif", 27.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.ForeColor = System.Drawing.Color.Gold
        Me.Label1.Location = New System.Drawing.Point(25, 98)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(129, 48)
        Me.Label1.TabIndex = 6
        Me.Label1.Text = "Hour"
        Me.Label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'Label2
        '
        Me.Label2.BackColor = System.Drawing.Color.Gold
        Me.Label2.Font = New System.Drawing.Font("Microsoft Sans Serif", 27.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.ForeColor = System.Drawing.Color.DeepPink
        Me.Label2.Location = New System.Drawing.Point(175, 98)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(142, 48)
        Me.Label2.TabIndex = 7
        Me.Label2.Text = "Minute"
        Me.Label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'Label3
        '
        Me.Label3.BackColor = System.Drawing.Color.DeepSkyBlue
        Me.Label3.Font = New System.Drawing.Font("Microsoft Sans Serif", 27.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.ForeColor = System.Drawing.Color.DarkBlue
        Me.Label3.Location = New System.Drawing.Point(341, 98)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(157, 48)
        Me.Label3.TabIndex = 8
        Me.Label3.Text = "Second"
        '
        'Label4
        '
        Me.Label4.BackColor = System.Drawing.SystemColors.Control
        Me.Label4.Font = New System.Drawing.Font("Algerian", 36.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.ForeColor = System.Drawing.Color.DeepPink
        Me.Label4.Location = New System.Drawing.Point(25, 21)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(473, 54)
        Me.Label4.TabIndex = 9
        Me.Label4.Text = "Timer"
        Me.Label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'Timer2
        '
        Me.Timer2.Interval = 1000
        '
        'Timer
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(526, 359)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.Button3)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.secondbox)
        Me.Controls.Add(Me.minutebox)
        Me.Controls.Add(Me.hourbox)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "Timer"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Timer"
        CType(Me.hourbox, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.minutebox, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.secondbox, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents hourbox As System.Windows.Forms.NumericUpDown
    Friend WithEvents minutebox As System.Windows.Forms.NumericUpDown
    Friend WithEvents secondbox As System.Windows.Forms.NumericUpDown
    Friend WithEvents Timer1 As System.Windows.Forms.Timer
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents Button3 As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents Timer2 As System.Windows.Forms.Timer

End Class
