def main():
    camel_case = input("camelCase: ")
    result = snakeify(camel_case)


def snakeify(cc):
    print("snake_case: ", end = "")
    #if uppercase then lowercase it and print underscore
    for char in cc:
        if char.isupper():
            print("_", end = "")
        new_char = char.lower()
        print(new_char, end = "")
    print("\n")

main()
