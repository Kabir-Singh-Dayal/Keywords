word = input("Enter a word")
char = input("Tell character to be selected")
for i in word:
    if i==char:
        print("Character", char, "has been found")
        break
    else:
        print("Character", char, "is not found")