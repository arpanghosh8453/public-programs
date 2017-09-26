#---------------------------------------------<class-Scale>--------------------------------------------#
class Scale(object):
    def __init__(self,symbol,water_freeze,water_boil):
        self.name = symbol
        self.ice = float(water_freeze)
        self.steam = float(water_boil)
        self.water = float(water_boil-water_freeze)
        if water_boil<water_freeze or water_freeze==water_boil:
            raise Exception("boiling temperature must be grater than freezing temperature")

    def is_indentical(self,scale):
        '''returns true only if the two scales are equivalent but the symbol may not be same'''
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        if self.ice == scale.ice and self.steam == scale.steam :
            return True
        else:
            return False

    def find_absolute(self):
        '''returns the absolute zero temperature with respect to its scale'''
        return absolute_zero.convert(self).value
    
    def equivalant_point(self,scale):
        '''returns the temperature where the value is same in both of the scales'''
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = float(scale.water)/float(self.water)
        if ratio == 1.0:
            return None
        return float(scale.ice-(ratio*self.ice))/float(1-ratio)
    
    def  scale_to_scale(self,new_scale_name,self_temp_pair,new_temp_pair):
        '''returns a scale object with the symbol as new_scale_name and the pairs of temperatures
given'''
        v1,v2 = float(self_temp_pair[0]),float(self_temp_pair[1])
        sv1,sv2 = float(new_temp_pair[0]),float(new_temp_pair[1])
        if v1 == v2 or sv1 == sv2:
            raise Exception("Values must not be equal ! ")
        if (sv2>sv1 and v1>v2)or(sv1>sv2 and v2>v1):
            raise Exception("values are incorrect ! ")
        if v1>v2:
            v1,v2 = v2,v1
            sv1,sv2 = sv2,sv1
        ratio = float(sv2-sv1)/float(v2-v1)
        if v1>self.ice:
            freeze = sv1-((v1-self.ice)*ratio)
        else:
            freeze = sv1+((self.ice-v1)*ratio)
        if v2>self.steam:
            boil = sv2-((v2-self.steam)*ratio)
        else:
            boil = sv2+((self.steam-v2)*ratio)
            
        return Scale(new_scale_name,freeze,boil)
    
    def compare_unit(self,scale):
        '''compares the unit values of the given scale with respect to self and returns the ratio of the
scale units'''
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = float(scale.steam-scale.ice)/float(self.steam-self.ice)
        return ratio



#---------------------------------------------<class-Temperature>--------------------------------------------#


class Temperature(object):
    def __init__(self,value,scale):
        self.value = float(value)
        self.scale = scale
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        
    def set_temperature(self,value):
        '''sets the tempareture keeping the scale same'''
        value = float(value)
        self.value = value

    def set_scale(self,scale):
        '''sets the scale keeping the tempareture same'''
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        self.scale = scale

    def show(self):
        '''shows the value of tempareture in a user-friendly manner with the scale symbol'''
        print self.value,self.scale.name

    def is_valid(self):
        '''returns true only if the tempareture is higher or equals to the absolute zero tempareture
in its scale'''
        if self.value<self.scale.find_absolute():
            return False
        else:
            return True
        
    def increase_temperature(self,value):
        '''increases the value of tempareture with respect to the given value, If the value is negative the tempareture
gets reduced by the given value'''
        value = float(value)
        self.value = self.value + value
        
    def convert(self,scale):
        '''converts the tempareture in the given scale and returns a Temperature object'''
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = self.scale.compare_unit(scale)
        temp = self.value
        new_value = (ratio*(temp-self.scale.ice))+scale.ice
        return Temperature(new_value,scale)
    
    def difference(self,temp_object):
        '''calculets the difference between the temparetures converting the given temp_object
into self scale and returns a Temperature object with the difference value'''
        if type(temp_object) != Temperature:
            raise Exception("Error in Temperature object ! ")
        converted = temp_object.convert(self.scale)
        value = self.value-converted.value
        return Temperature(value,self.scale)
    
    def is_equivelent(self,temp_object):
        '''returns true only if the given object's value and self value matches, it checks the scale
conversion autometically'''
        if type(temp_object) != Temperature:
            raise Exception("Error in Temperature object ! ")
        converted = temp_object.convert(self.scale)
        if self.value == converted.value:
            return True
        else:
            return False
        
        
#---------------------------------------#some standerd scales and temparetures#-------------------------------#
        
        
C_scale = Scale("centigrade",0,100)
F_scale = Scale("farenheite",32,212)
K_scale = Scale("kelvin",273,373)
absolute_zero = Temperature(0,K_scale)
human_body_temp = Temperature(98.4,F_scale)


#------------------------------------------#module check#-----------------------------------------------#

if __name__ == '__main__':
    print C_scale.find_absolute()
    print F_scale.find_absolute()
    t = Temperature(36.8888888888888888,C_scale)
    t.show()
    t1 = t.convert(F_scale)
    t1.show()
    print C_scale.compare_unit(F_scale)
    print t.is_equivelent(t1)
    t2 = Temperature(180,C_scale)
    print t2.difference(t1).value
    t3 = Temperature(156235,C_scale)
    print t3.is_valid()



                
