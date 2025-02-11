import math

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    
    def __add__(self, other):
        lcm = math.lcm(self.bottom, other.bottom)
        left_multiplier = lcm / self.bottom
        right_multiplier = lcm / self.top

        return Fraction(int(self.top * left_multiplier + other.top * right_multiplier), lcm)

    def __sub__(self, other):
        lcm = math.lcm(self.bottom, other.bottom)
        left_multiplier = lcm / self.bottom
        right_multiplier = lcm / self.top

        return Fraction(int(self.top * left_multiplier - other.top * right_multiplier), lcm)
    
    def __mul__(self, other):
        return Fraction(self.top * other.top, self.bottom * other.bottom)
    
    def __truediv__(self, other):
        return Fraction(self.top * other.bottom, self.bottom * other.top) 
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.top / self.bottom == other.top / other.bottom
        elif isinstance(other, int) or isinstance(other, float):
            return self.top / self.bottom == other
        else:
            return NotImplemented
    
    def __ne__(self, other):
        return self.top / self.bottom != other.top / other.bottom
    
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.top / self.bottom > other.top / other.bottom
        elif isinstance(other, int) or isinstance(other, float):
            return self.top / self.bottom > other
        else:
            return NotImplemented
        
    def __lt__(self, other):
        return self.top / self.bottom < other.top / other.bottom
    
    def __ge__(self, other):
        return self.top / self.bottom >= other.top / other.bottom
    
    def __le__(self, other):
        return self.top / self.bottom <= other.top / other.bottom
    
    def __int__(self):
        if (self.top % self.bottom) == 0:
            return (int(self.top / self.bottom))
        else:
            raise ValueError('Error! Not a whole number!')
    
    def __float__(self):
        return self.top / self.bottom
    
    def __str__(self):
        return f'{self.top}/{self.bottom}'
    
    def __repr__(self):
        return f'Fraction({self.top}, {self.bottom})'
    
    def __bool__(self):
        if self.top == 0:
            return False
        else:
            return True
        
    def __format__(self, format_spec):
        if format_spec == 'regular':
            return self.__str__()
        elif format_spec == 'long':
            return f'{self.top} over {self.bottom}'
        elif format_spec == 'reduced':
            gcd = math.gcd(self.top, self.bottom)
            return f'{int(self.top / gcd)}/{int(self.bottom / gcd)}'
        else:
            return self.__str__()
        
f1 = Fraction(2, 4)
f2 = Fraction(8, 2)
f3 = Fraction(2, 3)

print(format(f1, 'regular'))
print(format(f1, 'long'))
print(format(f1, 'reduced'))
