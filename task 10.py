def common_words(str1, str2):


    s1 = set(str1)

    s2 = set(str2)

    string = {s1 , s2}

    print("Common letter: {}" .join(string))



common_words("aeroplane", "spaceship")
