def area_of_triangle(x, y, z):

    s = ((x + y + z) / 2)

    area = (s*(s - x) * (s - y) * (s - z))**0.5

    print(area)



area_of_triangle(16,20,30)
