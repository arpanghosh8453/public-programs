class Scale(object):
    def __init__(self,symbol,water_freeze,water_boil):
        self.name = symbol
        self.ice = float(water_freeze)
        self.steam = float(water_boil)
        self.water = float(water_boil-water_freeze)
        if water_boil<water_freeze or water_freeze==water_boil:
            raise Exception("boiling temperature must be grater than freezing temperature")

    def is_indentical(self,scale):
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        if self.ice == scale.ice and self.steam == scale.steam :
            return True
        else:
            return False

    def find_absolute(self):
        return absolute_zero.convert(self).value
    
    def equivalant_point(self,scale):
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = float(scale.water)/float(self.water)
        if ratio == 1.0:
            return None
        return float(scale.ice-(ratio*self.ice))/float(1-ratio)
    
    def  scale_to_scale(self,new_scale_name,self_temp_pair,new_temp_pair):
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
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = float(scale.steam-scale.ice)/float(self.steam-self.ice)
        return ratio





class Temperature(object):
    def __init__(self,value,scale):
        self.value = float(value)
        self.scale = scale
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        
    def set_temperature(self,value):
        value = float(value)
        self.value = value

    def set_scale(self,scale):
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        self.scale = scale

    def show(self):
        print(self.value,self.scale.name)

    def is_valid(self):
        if self.value<self.scale.find_absolute():
            return False
        else:
            return True
        
    def increase_temperature(self,value):
        value = float(value)
        self.value = self.value + value
        
    def convert(self,scale):
        if type(scale) != Scale:
            raise Exception("Error in scale object ! ")
        ratio = self.scale.compare_unit(scale)
        temp = self.value
        new_value = (ratio*(temp-self.scale.ice))+scale.ice
        return Temperature(new_value,scale)
    
    def difference(self,temp_object):
        if type(temp_object) != Temperature:
            raise Exception("Error in Temperature object ! ")
        converted = temp_object.convert(self.scale)
        value = self.value-converted.value
        return Temperature(value,self.scale)
    
    def is_equivelent(self,temp_object):
        if type(temp_object) != Temperature:
            raise Exception("Error in Temperature object ! ")
        converted = temp_object.convert(self.scale)
        if self.value == converted.value:
            return True
        else:
            return False
        
        

C_scale = Scale("centigrade",0,100)
F_scale = Scale("farenheite",32,212)
K_scale = Scale("kelvin",273,373)
absolute_zero = Temperature(0,K_scale)
human_body_temp = Temperature(98.4,F_scale)




if __name__ == '__main__':
    print(C_scale.find_absolute())
    print(F_scale.find_absolute())
    t = Temperature(36.8888888888888888,C_scale)
    t.show()
    t1 = t.convert(F_scale)
    t1.show()
    print(C_scale.compare_unit(F_scale))
    print(t.is_equivelent(t1))
    t2 = Temperature(180,C_scale)
    print(t2.difference(t1).value)
    t3 = Temperature(156235,C_scale)
    print(t3.is_valid())



                
