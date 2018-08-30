import matplotlib.pyplot as plt
import math
import sympy as sp
from sympy.abc import mu,i,A
import numpy as np

#***************************************************GLOBAL VALUES*************************************************************

# main function of deviation (delta)
f = sp.deg(sp.asin(mu*sp.sin(A-sp.asin(sp.sin(i)/mu)))+i-A)

 #taking all values for incident angle
all_values = np.linspace(0.00001,90.0,100)


#***************************************************Normal Graph [ delta vs i ] *****************************************************


# ------------------------------------------------Delta vs incident angle ( in varying mu )---------------------------------------------------------

# for mu =1.5 & A = 60
y_list = []
x_list = []
for v in all_values:
    try:
        #only possible values should be taken
        y_list.append(float(f.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.5})))
        x_list.append(v)
    except:
        pass
    
# for mu =1.33 & A = 60
y1_list = []
x1_list = []
for v in all_values:
    try:
        y1_list.append(float(f.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.33})))
        x1_list.append(v)
    except:
        pass
    
# for mu =root(3) & A = 60
y2_list = []
x2_list = []
for v in all_values:
    try:
        y2_list.append(float(f.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:math.sqrt(3)})))
        x2_list.append(v)
    except:
        pass

# Plotting of delta vs i (in varying mu)
plt.plot(x1_list,y1_list,label = "mu = 1.33(water)")
plt.plot(x_list,y_list,label = "mu = 1.5(glass)")
plt.plot(x2_list,y2_list,label = "mu = root(3)")
plt.grid()
plt.legend()
plt.show()

# ------------------------------------------------Delta vs incident angle ( in varying A )---------------------------------------------------------

#for A = 50 & mu = 1.5
y3_list = []
x3_list = []
for v in all_values:
    try:
        y3_list.append(float(f.evalf(subs = {i:sp.rad(v),A:sp.rad(50),mu:1.5})))
        x3_list.append(v)
    except:
        pass
    
#for A = 70 & mu = 1.5
y4_list = []
x4_list = []
for v in all_values:
    try:
        y4_list.append(float(f.evalf(subs = {i:sp.rad(v),A:sp.rad(70),mu:1.5})))
        x4_list.append(v)
    except:
        pass

# Plotting of delta vs i (in varying A)
plt.plot(x3_list,y3_list,label = "A = 50")
plt.plot(x_list,y_list,label = "A = 60")
plt.plot(x4_list,y4_list,label = "A = 70")
plt.grid()
plt.legend()
plt.show()


#************************************************ Differentiation [ d(delta)/d(i) ]  < 1st order >***************************************************

f2 = sp.diff(f,i,1)#differentiating function f (delta func w.r.t. i) w.r.t. i  in 1st order .... e.g. -- > d(delta)/d(i)

# ------------------------------------------------d(delta)/d(i) vs incident angle ( in varying mu )---------------------------------------------------------

# for mu =1.5 & A = 60
y_diff_list = []
x_diff_list = []
for v in all_values:
    try:
        #only possible values should be taken
        y_diff_list.append(float(f2.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.5})))
        x_diff_list.append(v)
    except:
        pass

# for mu =1.33 & A = 60
y1_diff_list = []
x1_diff_list = []
for v in all_values:
    try:
        y1_diff_list.append(float(f2.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.33})))
        x1_diff_list.append(v)
    except:
        pass
    
# for mu =root(3) & A = 60
y2_diff_list = []
x2_diff_list = []
for v in all_values:
    try:
        y2_diff_list.append(float(f2.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:math.sqrt(3)})))
        x2_diff_list.append(v)
    except:
        pass

# Plotting of delta vs i (in varying mu)    
plt.plot(x1_diff_list,y1_diff_list,label = "mu = 1.33(water)")
plt.plot(x_diff_list,y_diff_list,label = "mu = 1.5(glass)")
plt.plot(x2_diff_list,y2_diff_list,label = "mu = root(3)")
plt.grid()
plt.legend()
plt.show()

# ------------------------------------------------d(delta)/d(i) vs incident angle ( in varying A )---------------------------------------------------------

#for A = 50 & mu = 1.5
y3_diff_list = []
x3_diff_list = []
for v in all_values:
    try:
        y3_diff_list.append(float(f2.evalf(subs = {i:sp.rad(v),A:sp.rad(50),mu:1.5})))
        x3_diff_list.append(v)
    except:
        pass
    
#for A = 70 & mu = 1.5
y4_diff_list = []
x4_diff_list = []
for v in all_values:
    try:
        y4_diff_list.append(float(f2.evalf(subs = {i:sp.rad(v),A:sp.rad(70),mu:1.5})))
        x4_diff_list.append(v)
    except:
        pass

# Plotting of delta vs i (in varying A)
plt.plot(x3_diff_list,y3_diff_list,label = "A = 50")
plt.plot(x_diff_list,y_diff_list,label = "A = 60")
plt.plot(x4_diff_list,y4_diff_list,label = "A = 70")
plt.grid()
plt.legend()
plt.show()


#************************************************ Differentiation [ d2(delta)/d(i)2 ]  < 2nd order >***************************************************

f3 = sp.diff(f,i,2)#differentiating function f (delta func w.r.t. i) w.r.t. i  in 2nd order .... e.g. -- > d2(delta)/d(i)2

# ------------------------------------------------d2(delta)/d(i)2 vs incident angle ( in varying mu )--------------------------------------------------------------------
# for mu =1.5 & A = 60
y_diff_list_1 = []
x_diff_list_1 = []
for v in all_values:
    try:
        #only possible values should be taken
        y_diff_list_1.append(float(f3.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.5})))
        x_diff_list_1.append(v)
    except:
        pass

# for mu =1.33 & A = 60
y1_diff_list_2 = []
x1_diff_list_2 = []
for v in all_values:
    try:
        y1_diff_list_2.append(float(f3.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:1.33})))
        x1_diff_list_2.append(v)
    except:
        pass
    
# for mu =root(3) & A = 60
y2_diff_list_3 = []
x2_diff_list_3 = []
for v in all_values:
    try:
        y2_diff_list_3.append(float(f3.evalf(subs = {i:sp.rad(v),A:sp.rad(60),mu:math.sqrt(3)})))
        x2_diff_list_3.append(v)
    except:
        pass

# Plotting of delta vs i (in varying mu)    
plt.plot(x1_diff_list_2,y1_diff_list_2,label = "mu = 1.33(water)")
plt.plot(x_diff_list_1,y_diff_list_1,label = "mu = 1.5(glass)")
plt.plot(x2_diff_list_3,y2_diff_list_3,label = "mu = root(3)")
plt.grid()
plt.legend()
plt.show()

# ------------------------------------------------d2(delta)/d(i)2 vs incident angle ( in varying A )---------------------------------------------------------

#for A = 50 & mu = 1.5
y3_diff_list_1 = []
x3_diff_list_1 = []
for v in all_values:
    try:
        y3_diff_list_1.append(float(f3.evalf(subs = {i:sp.rad(v),A:sp.rad(50),mu:1.5})))
        x3_diff_list_1.append(v)
    except:
        pass
    
#for A = 70 & mu = 1.5
y4_diff_list_2 = []
x4_diff_list_2 = []
for v in all_values:
    try:
        y4_diff_list_2.append(float(f3.evalf(subs = {i:sp.rad(v),A:sp.rad(70),mu:1.5})))
        x4_diff_list_2.append(v)
    except:
        pass

# Plotting of delta vs i (in varying A)
plt.plot(x3_diff_list_1,y3_diff_list_1,label = "A = 50")
plt.plot(x_diff_list_1,y_diff_list_1,label = "A = 60")
plt.plot(x4_diff_list_2,y4_diff_list_2,label = "A = 70")
plt.grid()
plt.legend()
plt.show()


# ************************************************************* Delta vs Prism angle****************************************************************

all_values_1 = np.linspace(5,100,100)#all prisam angles

#-------------------------------------------------plotting of Delta vs Prism angle in varying incident angle----------------------------------------------------

#for i = 30 & mu = 1.5
y6_list = []
x6_list = []
for v in all_values_1:
    try:
        y6_list.append(float(f.evalf(subs = {i:sp.rad(30),A:sp.rad(v),mu:1.5})))
        x6_list.append(v)
    except:
        pass

#for i = 50 & mu = 1.5
y7_list = []
x7_list = []
for v in all_values_1:
    try:
        y7_list.append(float(f.evalf(subs = {i:sp.rad(50),A:sp.rad(v),mu:1.5})))
        x7_list.append(v)
    except:
        pass

#for i = 70 & mu = 1.5
y8_list = []
x8_list = []
for v in all_values_1:
    try:
        y8_list.append(float(f.evalf(subs = {i:sp.rad(70),A:sp.rad(v),mu:1.5})))
        x8_list.append(v)
    except:
        pass

#plotting of Delta vs Prism angle in varying incident angle
plt.plot(x6_list,y6_list,label = "i = 30")
plt.plot(x7_list,y7_list,label = "i = 50")
plt.plot(x8_list,y8_list,label = "i = 70")
plt.grid()
plt.legend()
plt.show()


# ****************************************************************Delta vs mu***************************************************************

all_values_2 = np.linspace(1,3,100)#all mu between 1 & 3

#-------------------------------------------------plotting of Delta vs mu in varying incident angle----------------------------------------------------

#for i = 30 & A = 60

f = sp.deg(sp.asin(mu*sp.sin(A-sp.asin(sp.sin(i)/mu)))+i-A)

y9_list = []
x9_list = []
for v in all_values_2:
    try:
        y9_list.append(float(f.evalf(subs = {i:sp.rad(30),A:sp.rad(60),mu:v})))
        x9_list.append(v)
    except:
        pass

#for i = 50 & A = 60
y10_list = []
x10_list = []
for v in all_values_2:
    try:
        y10_list.append(float(f.evalf(subs = {i:sp.rad(50),A:sp.rad(60),mu:v})))
        x10_list.append(v)
    except:
        pass

#for i = 70 & A = 60
y11_list = []
x11_list = []
for v in all_values_2:
    try:
        y11_list.append(float(f.evalf(subs = {i:sp.rad(70),A:sp.rad(60),mu:v})))
        x11_list.append(v)
    except:
        pass

#plotting of Delta vs mu in varying incident angle
plt.plot(x9_list,y9_list,label = "i = 30")
plt.plot(x10_list,y10_list,label = "i = 50")
plt.plot(x11_list,y11_list,label = "i = 70")
plt.grid()
plt.title("Plot of delta vs mu by Arpan Ghosh")
plt.legend()
plt.show()

#**************************************************************************************************************************
