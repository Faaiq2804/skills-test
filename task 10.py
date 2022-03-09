def common_words(word_1, word_2):

    s1 = set(word_1.lower())

    s2 = set(word_2.lower())

    list = (s1 & s2)

    for char in list:

        char = ', '.join(list)

    print("Common characters: ",char)

   

common_words("Liverpool", "BarcElona")
