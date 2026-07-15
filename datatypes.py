class Own_data_types:
    
    def __init__(self,a,b):
        self.num=a
        self.den=b
    def __str__(self):
        return (f"{self.num}/{self.den}")
    def __add__(self,other):
        temp_num=self.num*other.den+self.den*other.num
        temp_den=self.den*other.den
        return Own_data_types(temp_num,temp_den)
    def __sub__(self,other):
        temp_num=self.num*other.den-self.den*other.num
        temp_den=self.den*other.den
        return Own_data_types(temp_num,temp_den)
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return Own_data_types(temp_num,temp_den)
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return Own_data_types(temp_num,temp_den)
F1=Own_data_types(23,4)
F2=Own_data_types(12,8)
print(F1)
print(F2)

print(F1+F2)
print(F1*F2)
print(F1-F2)
print(F1/F2)


        