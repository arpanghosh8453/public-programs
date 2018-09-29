#-----------------------------------------Imports------------------------------------------------------
from math import sqrt,cos,acos,degrees,radians



#--------------------------------------------Error Definitions-----------------------------------------

class DirectionError(TypeError):
    '''initializes a direction error'''
    def __init__(self,msg):
        super(DirectionError,self).__init__(msg)

class VectorError(TypeError):
    '''initializes a vector error'''
    def __init__(self,msg):
        super(VectorError,self).__init__(msg)

def check_direction(direction):
    '''checks whether the given direction is a direction object'''
    if type(direction) != Direction:
        raise DirectionError(": a direction object must be supplied.")
    else:
        pass

def check_vector(vector):
    '''checks whether the given vector is a vector object'''
    if type(vector) != Vector:
        raise VectorError(": a vector object must be supplied.")
    else:
        pass




#------------------------------------------------Direction Class--------------------------------------------

class Direction(object):
    def __init__(self,x_angle,y_angle):
        '''initializes a vector object'''
        if (x_angle>180 or y_angle>180) or (x_angle<0 or y_angle<0):
            raise Exception("Angles must be within 0 to 180 degrees")
        try:
            value = 1-(cos(radians(x_angle))**2)-(cos(radians(y_angle))**2)
            if abs(value)<1e-15:
                value = 0
            z_cos = sqrt(value)
            z_angle = degrees(acos(z_cos))
        except Exception as e:
            raise e
            raise Exception("Direction angle are not correctly given!")
        self.x = float(x_angle)
        self.y = float(y_angle)
        self.z = float(z_angle)

    def dictionary_degrees(self):
        return {'X':self.x,'Y':self.y,'Z':self.z}
    
    def dictionary_radians(self):
        return {'X':radians(self.x),'Y':radians(self.y),'Z':radians(self.z)}

    def dictionary_cosines(self):
        values = self.dictionary_radians()
        return {'X':cos(values['X']),'Y':cos(values['Y']),'Z':cos(values['Z'])}

    def is_equal(self,direction):
        check_direction(direction)
        if self.dictionary_cosines() == direction.dictionary_cosines():
            return True
        else:
            return False



#------------------------------------------------Vector Class------------------------------------------------

class Vector(object):
    def __init__(self,Xi,Yj,Zk):
        self.i = float(Xi)
        self.j = float(Yj)
        self.k = float(Zk)

    def magnitude(self):
        return float(sqrt((self.i**2)+(self.j**2)+(self.k**2)))

    def unit_vector(self):
        if self.magnitude() != 0:
            return Vector(self.i/self.magnitude(),self.j/self.magnitude(),self.k/self.magnitude())
        else:
            raise VectorError(" : No defined unit vector for null vector!")

    def direction(self):
        if self.magnitude() != 0:
            x_angle = degrees(acos(self.i/self.magnitude()))
            y_angle = degrees(acos(self.j/self.magnitude()))
            return Direction(x_angle,y_angle)
        else:
            raise VectorError(" : No defined direction for null vector!")

    def is_parallel(self,vector):
        check_vector(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise VectorError(" : Undefined comparison with null vector!")
        else:
            direction_self = self.direction()
            direction_other = vector.direction()
            if direction_self.is_equal(direction_other):
                return True
            else:
                return False

    def is_equal(self,vector):
        check_vector(vector)
        if (self.magnitude() == 0) and (vector.magnitude() == 0):
            return True
        elif (self.magnitude() == 0) or (vector.magnitude() == 0):
            return False
        elif (self.is_parallel(vector))and(self.magnitude() == vector.magnitude()):
            return True
        else:
            return False

    def __neg__(self):
        return Vector(-self.i,-self.j,-self.k)

    def is_opposite(self,vector):
        check_vector(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise VectorError(" : Undefined comparison with null vector!")
        if vector.is_equal(self.__neg__()):
            return True
        else:
            return False

    def is_antiparallel(self,vector):
        check_vector(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise VectorError(" : Undefined comparison with null vector!")
        if vector.direction().is_equal(self.__neg__().direction()):
            return True
        else:
            return False

    def __add__(self,vector):
        check_vector(vector)
        i = (self.i+vector.i)
        j = (self.j+vector.j)
        k = (self.k+vector.k)
        return Vector(i,j,k)

    def __sub__(self,vector):
        check_vector(vector)
        opposite = vector.__neg__()
        return self.__add__(opposite)


    def __mul__(self,vector):
        if type(vector) == float or type(vector) == int:
            num = float(number)
            i = num*self.i
            j = num*self.j
            k = num*self.k
            return Vector(i,j,k)
        else:
            check_vector(vector)
            return (self.i*vector.i+self.j*vector.j+self.k+vector.k)

    def __pow__(self,vector):
        check_vector(vector)
        i = (self.j*vector.k-self.k*vector.j)
        j = (self.k*vector.i-self.i*vector.k)
        k = (self.i*vector.j-self.j*vector.i)
        return Vector(i,j,k)

    def angle_between(self,vector):
        check_vector(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise VectorError(" : No angle can be measured with null vector!")
        else:
            divisor = self.magnitude()*vector.magnitude()
            dot = self.__mul__(vector)
            return degrees(acos(dot/divisor))

    def is_perpendicular(self,vector):
        check_vector(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise VectorError(" : Undefined comparison with null vector!")
        else:
            if self.__mul__(vector) == 0:
                return True
            else:
                return False

    def component(self,direction):
        check_direction(direction)
        unit = create_vector(1,direction)
        angle = self.angle_between(unit)
        value = self.magnitude()*cos(radians(angle))
        return unit.__mul__(value)

    def is_coplanar(self,vector1,vector2):
        check_vector(vector1)
        check_vector(vector2)
        if (vector1.__pow__(vector2)).__mul__(self) == 0:
            return True
        else:
            return False
        





#----------------------------------------------Functions---------------------------------------------------
def create_vector(magnitude,direction):
    value = float(magnitude)
    check_direction(direction)
    dictionary = direction.dictionary_radians()
    x = value*cos(dictionary['X'])
    y = value*cos(dictionary['Y'])
    z = value*cos(dictionary['Z'])
    return Vector(x,y,z)



#--------------------------------------------Module Checkup---------------------------------------------
if __name__ == '__main__':
    x = Direction(45,45)
    y = Direction(45,45)
    z = Direction(108,46)
    v = Vector(1,2,3)
    v1 = create_vector(45,z)
    '''print x.is_equal(y)
    print x.is_equal(z)
    print v.magnitude()
    print v.direction().dictionary_degrees()
    print v.opposite().magnitude()
    print v.opposite().direction().dictionary_degrees()
    print v.is_opposite(v.opposite())
    print v.is_antiparallel(v.opposite())
    print v.unit_vector().magnitude()
    print v1.magnitude()
    print v+v1'''
    #print (v-v1).magnitude()
    print(-v)







        
