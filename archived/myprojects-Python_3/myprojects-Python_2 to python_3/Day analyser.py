y = eval(input("enter the year :"))
m = eval(input("enter the month number :"))
d = eval(input("enter the date :"))
if y<=0 or m<=0 or m>12 or d<=0 or d>31:
    raise ValueError("Error values!!")
if y%100 == 0 and y%400 == 0:
    ly = 1
elif y%100>0 and y%4 == 0:
    ly = 1
else:
    ly = 0
ye = y%100
ys = (y//100)%4
x = ye//4
l1 = (6,4,2,0)
l = l1[ys]
mn = [1,4,4,0,2,5,0,3,6,1,4,6]
if ly:
    mn[0] = 0
    mn[1] = 3
a = (m-1)
n = mn[a]
r = (ye+x+l+n+d)%7
dl = ("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")
print("\nThe day is",dl[r])
i = input("ESC :")
