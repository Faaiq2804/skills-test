def vowels_only(word):


    list_vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    for i in word:

        if i not in list_vowels:

            word = word.replace(i, " ")

    print(word)

vowels_only("FaaiqAbrahams")
