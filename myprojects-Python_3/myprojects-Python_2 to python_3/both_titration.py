import matplotlib.pyplot as plt
from math import log10,sqrt
from numpy import arange

KW = 10**-14
acid_conc = 0.1
acid_ml = 50

base_conc = 0.1
base_ml_list = arange(0,80,0.1)


ph = []

for ml in base_ml_list:
    conc = float(acid_conc * acid_ml - base_conc * ml)/float(acid_ml+ml)+sqrt(KW)
    if conc >= 0:
        value = -log10(conc)
    else:
        value = (-log10(KW))+log10(abs(conc))

    ph.append(value)

plt.plot(base_ml_list,ph,label = "Acid(HCl) & Base(NaOH)")


PKW = 14
wa_ml = 50
wa_conc = 0.1
wa_pka = 4.744727495
init_ph = 0.5*(wa_pka - log10(wa_conc))
print(init_ph)
sb_ml_list = arange(0,80,0.1)
ph_list = [init_ph]
sb_conc = 0.1

for ml in sb_ml_list:
    acid_mm = wa_ml * wa_conc
    base_mm = ml * sb_conc
    volume_ml = wa_ml + ml

    if ml == 0:
        continue
    acid_conc = (acid_mm-base_mm)/float(volume_ml)
    salt_conc = base_mm / float(volume_ml)
    if acid_conc == 0:
        ph = 0.5 * (PKW + wa_pka + log10(salt_conc))
    elif acid_conc < 0:
        base_conc = abs(acid_conc)
        ph = PKW + log10(base_conc)
    else:
        ph = wa_pka + log10(salt_conc/acid_conc)
        #print ph
        
    ph_list.append(ph)
        

plt.plot(sb_ml_list,ph_list,label = "Acid(CH3COOH) & Base(NaOH)")
plt.grid()
plt.legend()
plt.xlabel("Volume of NaOH(0.1 M) added in 50 ml CH3COOH or HCl(0.1 M)")
plt.ylabel("ph of the Resulting Solution")
plt.title("PLOT OF A ACID BASE TITRATION PLOTED BY ARPAN GHOSH")
plt.show()
