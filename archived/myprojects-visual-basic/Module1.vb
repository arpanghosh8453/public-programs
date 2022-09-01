Module Module1

    Sub Main()
        Console.WriteLine("Enter a positive number : ")
        Dim num As Long
        Dim value As Long
        Dim isprime As Boolean = True
        Dim enterloop As Boolean = True
        Try
            num = Console.ReadLine()
            If num = 2 Then
                Console.WriteLine("It is a prime number")
                enterloop = False
                Console.ReadLine()
            ElseIf num < 2 and Then
                Console.WriteLine("It is out of range!!")
                enterloop = False
                Console.ReadLine()
            End If
            If enterloop = True Then
                For value = 2 To num - 1
                    If num Mod value = 0 Then
                        Console.WriteLine("it is not a prime number : It is divisable with " & value)
                        isprime = False
                    End If
                Next
                If isprime = True Then
                    Console.WriteLine("It is a prime number")
                End If
                Console.ReadLine()
            End If
        Catch ex As Exception
            Console.WriteLine("End of programme!!")
            Console.WriteLine(ex)
            Console.ReadLine()
        End Try
        
            
    End Sub

End Module
