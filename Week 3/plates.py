import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    global x
    x = 0

    #check length of thing
    if len(s) < 7 and len(s) > 1:
        x += 1

        #first 2 characters are letters
        if s[0].isalpha() and s[1].isalpha():
            x += 1

        #ensures they are not in the middle
        index = 2
        for char in s[2: ]:
            if char.isdigit():
                z = s[index: ]
                if z.isdigit():
                    x += 1
                    break
            index += 1

        #check if s has any numbers
        if s.isalpha():
                x += 2

        #check if first number is 0
        for char in s[2: ]:
            if char.isdigit():
                if char != "0":
                    x += 1
                break


        #check for punctuation
        a = 0
        for char in s:
            if char in string.punctuation:
                a += 1
                break
        if a == 0:
            x += 1

    if x >= 5:
        return True
    else:
        return False

main()
