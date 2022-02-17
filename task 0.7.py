def convert_to_Fahrenheit(x):
    Celsius=x
    x = (Celsius*1.8)+32
    return x
    
print(convert_to_Fahrenheit(32))




def convert_to_Celsius(y):
     
    Fahrenheit = y
    y = (Fahrenheit - 32) * 0.556
    return y

print(convert_to_Celsius(110))
