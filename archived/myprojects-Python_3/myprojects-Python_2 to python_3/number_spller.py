#---------------------spells one,two and three digited numbers only--------------------
def partspell(num):
    if num == 0:return ''
    one = {1:'one ',2:'two ',3:'three ',4:'four ',5:'five ',6:'six ',7:'seven ',8:'eight ',
           9:'nine '}
    two = {2:'twenty ',3:'thirty ',4:'forty ',5:'fifty ',6:'sixty ',7:'seventy ',8:'eighty ',
           9:'ninety '}
    special = {10:'ten ',11:'eleven ',12:'twelve ',13:'thirteen ',14:'fourteen ',15:'fifteen ',
               16:'sixteen ',17:'seventeen ',18:'eighteen ',19:'nineteen '}
    spell = ''
    if num>=100:
        value = num//100
        num = num%100
        spell = spell+one[value]+'hundred '
    if num>19:
        value = num//10
        num = num%10
        spell = spell + two[value]
    if num in list(special.keys()):
        return spell + special[num]
    if num != 0:
        return spell + one[num]
    else:
        return spell

#-----------takes any digited number and parts it & send it to partspller function.----------------   
def main(num):
    if num == 0:return 'zero'
    spell = ''
    while num != 0:
        if len(str(num))>3:
            rem = num % 1000
            if rem != 0:
                spell= partspell(rem)+spell
            num = num // 1000
        else:
            return partspell(num)+spell
        #.............  for lakh and thousand counting............
        for count in ['thousand ','lakh ']:
            if len(str(num))>2:
                rem = num%100
                if rem != 0:
                    spell = partspell(rem)+count+spell
                num = num //100
            else:
                return partspell(num)+count+spell

        if num != 0:
            spell = 'crore '+spell
#----------------------------takes the number input only-------------------------
def takeinput():
    while True:
        try:
            number = int(input("Enter any positive whole number :"))
            if number >= 0:
                return number
            else:
                raise ValueError("Error")
        except:
            print("......ERROR!!......Please enter a valid number.........")
#--------------------------------calling the created functions-----------------------
while True:
    number = takeinput()#taking input........
    print('\n'+main(number))#printing result.......
    print('-'*70)
    #check for repeating...................
    repeat = input("Use Again??(y\\n):")
    if repeat != 'y':
        break
    else:
        print('-'*70)
    



            
        
                
