import math
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.length = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        
    def plus(self,vector):
        return Vec(self.x + vector.x, self.y + vector.y)
    
    def minus(self,vector):
        return Vec(self.x - vector.x, self.y - vector.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vec(1, 2).plus(Vec(2, 3)))

print(Vec(1, 2).minus(Vec(2, 3)))

print(Vec(3, 4).length)
