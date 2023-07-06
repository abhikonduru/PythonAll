def tallyChar(letter,input):
    length=len(input)
    occurrences=0
    for x in range(0,length):
        if input[x] == letter:
            occurrences+=1
    print("The letter %s occurs %s times in the word"%(letter, occurrences))

input = input("Enter text: ")
letter = input("Enter a character: ")

tallyChar(letter,input)