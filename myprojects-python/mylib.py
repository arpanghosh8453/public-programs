import math
class other:
    def listmaker(self,*args):
        l = []
        for i in args:
            try:
                for m in i:
                    l.append(m)
            except:
                l.append(i)
        return l
class mymath(other):
    def reverse(self,iterable_val):
        tp = type(iterable_val)
        if tp is int or long:
            return int(str(iterable_val)[::-1])
        elif tp is bool:
            if iterable_val is True:
                return False
            else:
                return True
        elif tp is str or list or tuple:
            return iterable_val[::-1]
        else:
            s = "{}object type not supported by reverse function".format(tp)
            raise TypeError(s)
    '''def factorial(self,integer):
        result = math.factorial(integer)
        return result'''
    def calculate_hcf(self,num):
        l =len(num)
        if l == 1:
            for i in num:return i
        elif l >= 2:
            x = num[0]
            for i in range(l-1):
                d = num[i+1]
                while d%x >0:
                    d,x = x,d%x
            return x
        else:
            raise ValueError('Function must contain at least one argument,0 found')
    def calculate_lcm(self,num):
        multiply = 1
        hcf = mymath.calculate_hcf(self,num)
        for i in num:
            multiply *= i
        return multiply/(hcf ** (len(num)-1))
    def lcm(self,*args):
        l = mymath.listmaker(self,*args)
        return mymath.calculate_lcm(self,l)
    def hcf(self,*args):
        l = mymath.listmaker(self,*args)
        return mymath.calculate_hcf(self,l)
    def root(self,number,root_power = 2):
        if number<0 and root_power%2 == 1 and root_power>0:
            number = (-1)* number
            d = 1
        elif number>0 and root_power>0:
            d = 0
        elif number == 0 and root_power>0:
            return 0
        else:
            raise ValueError('funcion must contain at least one argument and root_power must be grater than 0')
        p = (float(1)/root_power)
        r = number ** p
        if d:
            r = (-1)* r
        return r
    def is_pallindrome(self,value):
        if value == mymath.reverse(self,value):
            return True
        else:
            return False
    def ratio(self,*args):
        val = []
        l = mymath.listmaker(self,*args)
        h = mymath.calculate_hcf(self,l)
        for i in l: 
            val.append(i/h)
        return val
    def mean(self,*values):
		sumvalue = 0
		length = len(values)
    try:
        for i in values:
            sumvalue = sumvalue + i
            return (sumvalue/length)
    except:
        print('Error in values...')
        return None

    def median(self,*values):
        try:
            length = len(values)-1
            listval = list(values) 
            listval.sort()
            if length % 2 == 0:
                return listval[int(length/2)]
            else:
                half = int(length/2)
                return ((listval[half]+listval[half + 1])/2)
        except:
            print('Error in values...')
            return None

    def mode(self,*values):
        try:
            listval = list(values)
            count = 0
            for i in listval:
                if listval.count(i) > count:
                    count = listval.count(i)
                    grater = i
            return grater
        except:
            print('Error in values...')
            return None

            
         
    

    
        
        
        
        
        
            
        
            
        



































































































































































































































































































        l = len(number)
        if l == 1:
            for i in number:return i
        elif l >= 2:
            x = l[0]
            for i in range(len(l)):
                d = l[i+1]
                while d%x > 0:
                    d,x = x,d%x
            return x
        else:
            raise ValueError("function must contain at least one value ,0 found..")
        
        

            
