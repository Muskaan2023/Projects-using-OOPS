class create_Data_Types:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        if self.b >= 0:
            return f"({self.a}+{self.b}i)"
        else:
            return f"({self.a}{self.b}i)"
    
    def __add__(self,other):
        temp_a=self.a+other.a
        temp_b=self.b+other.b
        return create_Data_Types(temp_a,temp_b)
    def __sub__(self,other):
        temp_a=self.a-other.a
        temp_b=self.b-other.b
        return create_Data_Types(temp_a,temp_b)
    def __mul__(self,other):
        temp_a=self.a*other.a-self.b*other.b
        temp_b=self.a*other.b+self.b*other.a
        return create_Data_Types(temp_a,temp_b)
    def __truediv__(self,other):
        denominator = other.a**2 + other.b**2
        temp_a = (self.a * other.a + self.b * other.b) / denominator
        temp_b = (self.b * other.a - self.a * other.b) / denominator
        return create_Data_Types(temp_a,temp_b)
complex1=create_Data_Types(2,3)
complex2=create_Data_Types(4,8)

print(complex1)
print(complex2)
print(complex1+complex2)
print(complex1/complex2)
print(complex1*complex2)
print(complex1-complex2)