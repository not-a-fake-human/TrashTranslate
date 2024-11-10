#imports
import random
import string

while True:
    #variables
    textInput = input("TrashTranslate > ")
    LDSS = string.printable

    #lists
    textList = [char for char in textInput]
    LDSL = [char for char in LDSS]
    output = []

    #code
    for text in textList:
        num = random.randint(0, 99)
        char = LDSL[num]
        output.append(char)

    outputString = ''.join(output)
    print(outputString)
