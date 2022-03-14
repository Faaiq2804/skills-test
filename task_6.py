def max_num(numb1, numb2, numb3):
  if numb1>numb2 and numb1>numb3:
    return numb1
  elif numb2>numb1 and numb2>numb3:
    return numb2
  elif numb3>numb1 and numb3>numb2:
    return numb3
  elif numb1==numb2 and numb1>numb2:
    return "It's a tie!"
  elif numb1==numb3 and numb1>numb2:
    return "It's a tie!"
  else:
    return "It's a tie!"
print(max_num(-10, 0, 10))
print(max_num(2, 3, 3)
