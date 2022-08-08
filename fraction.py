class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.dem = d

    def __str__(self):
        return f'{self.num}/{self.dem}'

    def __add__(self, other):
        temp_num = self.num*other.dem + self.dem*other.num
        temp_dem = self.dem*other.dem
        return f'{temp_num}/{temp_dem}'

    def __sub__(self, other):
        temp_num = self.num*other.dem - self.dem*other.num
        temp_dem = self.dem*other.dem
        return f'{temp_num}/{temp_dem}'

    def __mul__(self, other):
        temp_num = self.num*other.dem
        temp_dem = self.dem*other.num
        return f'{temp_num}/{temp_dem}'

    def __truediv__(self, other):
        temp_num = self.num * other.dem + self.dem * other.num
        temp_dem = self.dem * other.dem
        return f'{temp_num}/{temp_dem}'




x = Fraction(5,6)
y = Fraction(7,10)

print(x, y)
print(x+y)
print(x*y)
print(x/y)
