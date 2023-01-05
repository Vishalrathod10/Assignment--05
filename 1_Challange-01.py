# CHALLANGE -01

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self.squaresum = (self.x**2) + (self.y**2) + (self.z**2)
        return f'sum_output = {self.squaresum}'

point_obj = point(1,3,5)
print(point_obj.sqSum())





