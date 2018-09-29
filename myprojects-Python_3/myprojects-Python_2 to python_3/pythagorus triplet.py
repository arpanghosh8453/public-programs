l = eval(input("Enter the limit of hypotenuse :"))
p = 2
q = 1
c = (p**2)+(q**2)
while c<= l:
    while p>q:
        a = (p**2)-(q**2)
        b = 2*p*q
        c = (p**2)+(q**2)
        if c>l:
            break
        print("(",a,",",b,",",c,")")
        q += 1
    q = 1
    p += 1
i = eval(input("ESC :"))
