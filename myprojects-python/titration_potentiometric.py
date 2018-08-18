import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy.abc import x

acid_C = 0.1
base_C = 0.1
acid_vol = 25
const = 10**-7

a = acid_C*acid_vol
b = base_C
c = acid_vol
z = const

def get_ph(base_vol):
    try:
        f = 14+sp.log(((b*x-a)/(c+x))+z,10)
        result = f.evalf(subs={x:base_vol})
        float(result)
        return result
        
    except:
        f = -sp.log(((a-b*x)/(c+x))+z,10)
        result = f.evalf(subs={x:base_vol})
        float(result)
        return result

def get_diff_ph(base_vol):
    try:
        if get_ph(base_vol) < 7:
            raise ValueError("Error")
        f = 14+sp.log(((b*x-a)/(c+x))+z,10)
        y = sp.diff(f,x)
        result = y.evalf(subs={x:base_vol})
        result = float(result)
        return result
        
    except:
        f = -sp.log(((a-b*x)/(c+x))+z,10)
        y = sp.diff(f,x)
        result = y.evalf(subs={x:base_vol})
        result = float(result)
        return result
    
def get_diff_2_ph(base_vol):
    try:
        if get_ph(base_vol) < 7:
            raise ValueError("Error")
        f = 14+sp.log(((b*x-a)/(c+x))+z,10)
        y = sp.diff(f,x,2)
        result = y.evalf(subs={x:base_vol})
        return result
        
    except:
        f = -sp.log(((a-b*x)/(c+x))+z,10)
        y = sp.diff(f,x,2)
        result = y.evalf(subs={x:base_vol})
        float(result)
        return result

def get_emf(ph):
    return 0.24+0.059*ph

def get_diff_emf(d_ph):
    return 0.059*d_ph


base_vol_list = np.linspace(0,50,1000)
ph_list =  map(get_ph,base_vol_list)
ph_diff_list_VOL = map(get_diff_ph,base_vol_list)
ph_diff_2_list_VOL = map(get_diff_2_ph,base_vol_list)
emf_list = map(get_emf,ph_list)
emf_diff_list_VOL = map(get_diff_emf,ph_diff_list_VOL)


plt.plot(base_vol_list,ph_diff_list_VOL)
plt.grid()


plt.plot(base_vol_list,ph_list)
plt.grid()


plt.plot(ph_list,emf_list)
plt.grid()


plt.plot(base_vol_list,emf_list)
plt.grid()



plt.plot(base_vol_list,emf_diff_list_VOL)
plt.grid()



plt.plot(base_vol_list,ph_diff_2_list_VOL)
plt.grid()



