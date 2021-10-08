def max_num(x, y, z):
  if x > y and x > z:
    return x
  elif y > x and y > z:
    return y
  elif z > x and z > y:
    return z
  elif x == y and x > z:
    return "It's a tie!"
  elif x == z and x > y:
    return "It's a tie!"
  else:
    return "It's a tie!"
print(max_num(-10, 0, 10))
print(max_num(2, 3, 3))
