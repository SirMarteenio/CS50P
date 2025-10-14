def main():
    x, y, z = input(": ").split(" ")
    x = int(x)
    z = int(z)
    math(x, y, z)

def math(a, b, c):
    if b == "+":
        ans = a + c
    elif b == "-":
        ans = a - c
    elif b == "*":
        ans = a * c
    elif b == "/":
        if c != 0:
            ans = a / c
        else:
            print("error - cannot divide by 0")
    print(float(ans))


main()
