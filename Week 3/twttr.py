def main():
    global word
    word = input("Input: ")
    shorten(word)


def shorten(a):
    list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    #check if input is member of 'list'
    for char in word:
        if char not in list:
            print(char, end = "")
    print()

main()
