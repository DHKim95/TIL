while True:
    words = input()

    if words == '#':
        break

    words = words.lower()
    print(words.count('a') + words.count('e') + words.count('i') + words.count('o') + words.count('u'))