def check_vowels(text):
  list=("a","e",'i',"o","u","A","E","I","O","U")
  word=""
  for char in text:
     if char in  list:
        if char!=word:
          word = word+char+" "
  return word
text= set('phIlosophy')
word=check_vowels(text).lower()
print("vowels:"+str(word))
