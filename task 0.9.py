word = "pizzA"
blank_word = ""
vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]

for letter in word:
  if letter in vowels:
    blank_word = letter
  print(blank_word)
