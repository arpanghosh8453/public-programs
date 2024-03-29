from math import *
import numpy as np
import matplotlib.pyplot as plt
repeat = int(input("Enter the number of functions : "))
print("\n" +"-" * 40 + "\n")
for i in range(repeat):
    start = float(input("Enter the starting value for "+str(i+1)+" Function : " ))
    end = float(input("Enter the ending value for "+str(i+1)+" Function : " ))
    step = float(input("Enter the step value for "+str(i+1)+" Function : " ))           
    x = np.arange(start,end,step)
    function = eval(input("Enter the "+str(i+1)+ " lambda function : "))
    func_name = input("Enter the function name : ")
    y = []
    for i in x:
        try:
            y.append(function(i))
        except Exception as error:
            raise ValueError("The given "+func_name+" function is not defined for x = "+str(i)+"\n"+str(error))
        
    plt.plot(x,y,label = func_name)
    plt.legend()
    print("\n" +"-" * 40 + "\n")

plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.title("PLOT OF 'Y' Vs. 'X' GRAPH")
plt.grid()
plt.show()
