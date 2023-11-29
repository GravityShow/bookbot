with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    counter = 0
    for i in words:
        counter += 1

def letterCount(words):
    counter = {}
    for word in words:
        letters = word   
        letters.split()
        for i in letters:
            i = i.lower()
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return counter

def reportPrint(output):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counter} words found in the document")
    print("")
    for letter in output:
        if letter.isalpha() == True:
            print(f"The {letter} character was found {output[letter]} times")
    print("--- End report ---")

reportPrint(letterCount(words))


        