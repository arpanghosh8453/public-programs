import random
l1=['names','ghosts','cow','goat','animal']
play=point=g=0
len1=len(l1)
while play==0:
    r=random.randint(0,(len1-1))
    str1=l1[r]
    l2=[]
    l3=[]
    g+=1
    for i in str1:
        l2.append(i)
    len2=len(l2)
    for i in range (len2):
        if l2[i]==" ":
            l3.append(" ")
        else:
            l3.append("_")
    chance=8
    while chance>0:
        flag=flag1=0
        for i in range (len2):
            print(l3[i], end=' ')
        print("\n")
        inp=input("enter ur choice:")
        for i in range (len2):
            if inp==l2[i]:
                l3[i]=inp
                flag=1
        if l2 == l3==0:
            print("u win")
            print("score",chance)
            flag1=1
            point+=chance
            break
        if flag==0:
            chance-=1
            print("wrong guess")
    if flag1!=1:
        print("u lose")
        point-=2
        print(str1)
        print("points now:",point)
    play=int(input("enter 0 to play:"))
print("total score",point)
print("times played",g)
print("average",(point/g))
        
        
    
