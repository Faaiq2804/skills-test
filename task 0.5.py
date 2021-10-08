a=5
b=8
c=9

a = float(input('5'))

b = float(input('8'))

c = float(input('9'))

s = (a + b + c)/2

Area = (s * (s - a) * (s - b) * (s - c))**0.5

print('The area of the triangle is %0.2f' %Area)