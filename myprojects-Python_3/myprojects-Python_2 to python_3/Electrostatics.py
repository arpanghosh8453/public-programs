from math import sqrt,pi
import matplotlib.pyplot as plt
import numpy
import random

class Vector(object):
    
    def __init__(self,x_comp,y_comp,z_comp):
        self.x = x_comp
        self.y = y_comp
        self.z = z_comp
        
    def __add__(self,vector):
        return Vector(self.x+vector.x,self.y+vector.y,self.z+vector.z)

    def magnitude(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
        
class Charge(object):
    def __init__(self,charge,position):
        self.charge = charge
        self.coordinate = position
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.z_pos = position[2]

class System():
    def __init__(self,*charges):
        self.charges = list(charges)
        self.di_electric_const = 1/(4*pi*(9*10**9))
        
    def get_potential(self,coordinate):
        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        constant = 1/(4*pi*self.di_electric_const)
        value = 0
        for charge in self.charges:
            distance = sqrt((charge.x_pos-x)**2 + (charge.y_pos-y)**2 + (charge.z_pos-z)**2)
            if distance == 0:
                raise ValueError("Error in distance value")
            value += (constant*float(charge.charge))/distance
        return value

    def add_charge(self,charge):
        self.charges.append(charge)

    def get_field(self,coordinate):
        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        constant = 1/(4*pi*self.di_electric_const)
        value = Vector(0,0,0)
        for charge in self.charges:
            distance = sqrt((charge.x_pos-x)**2 + (charge.y_pos-y)**2 + (charge.z_pos-z)**2)
            if distance == 0:
                raise ValueError("Error in distance value")
            magnitude = (constant*charge.charge)/float(distance**2)
            x_comp = (magnitude*(x-charge.x_pos))/float(distance)
            y_comp = (magnitude*(y-charge.y_pos))/float(distance)
            z_comp = (magnitude*(z-charge.z_pos))/float(distance)
            value += Vector(x_comp,y_comp,z_comp)
            
        return value.magnitude()

    
def plot_graph(system):

    x = numpy.linspace(-20,20,1000)
    potential = []
    field = []

    for i in x:
        potential.append(system.get_potential((i,0,0)))
        field.append(system.get_field((i,0,0)))

    plt.plot(x,potential,label = "Electostatic Potential")
    plt.legend()
    plt.plot(x,field, label = "Electostatic Field" )
    plt.legend()
    plt.xlabel("Position of the test charge")
    plt.ylabel("Intensity")
    plt.title("Plot of Electostatic Field and Potential graph")
    plt.grid()
    plt.show()
    #plt.savefig(r"D:\pictures\newfig_"+str(j)+".png")
    #plt.close()


#for symmetrical charge distribution

c1 = Charge(-5.00,(0,1,1))
c2 = Charge(-5.00,(0,-1,1))
c3 = Charge(-5.00,(0,1,-1))
c4 = Charge(-5.00,(0,-1,-1))
system = System(c1,c2,c3,c4)
plot_graph(system)

#for random charge distribution
'''
for j in range(30):
    system = System(Charge(0,(0,1,1)))
    for i in range(50):
        charge = random.randint(-5,5)
        position = (0,random.randint(0,10)*random.random(),random.randint(0,10)*random.random())
        system.add_charge(Charge(charge,position))
    plot_graph(system)
'''
#for a rod along (x = 0,y = -1 ==> +1,z = 1)
'''
charge = 5
length = 2
charge_density = charge/float(length)
system = System(Charge(0,(0,0,0)))
increment = 0.01
delta_charge = charge_density*increment
increasing_value = 0
x = 0
y = -1
z = 1
while increasing_value < length:
    system.add_charge(Charge(delta_charge,(x,y,z)))
    y += increment
    increasing_value += increment
plot_graph(system)
'''
    
    
    
    
    
