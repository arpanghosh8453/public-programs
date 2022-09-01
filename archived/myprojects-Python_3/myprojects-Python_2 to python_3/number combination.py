import time
n = eval(input("Enter the number please :"))
n = int(n)
l = []
print_list = []
c = st =0
while n>0:
    l.append(str(n%10))
    n //= 10
l.sort()
l.reverse()
d = int("".join(l))
m = d
while m>0:
    a = m%10
    st = (st*10)+a
    m //= 10
e = str(st)

while st<=d:
    t = str(d)
    for i in e:
        if t.count(i) == e.count(i):
            m = 1
        else:
            m = 0
            break
    if m:
        print_list.append(d)
        c +=1
    d -= 9
print_list.reverse()
for i in print_list:
    print(i)
print("Total Combination :",c)
while True:
    time.sleep(5)


