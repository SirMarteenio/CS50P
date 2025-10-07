def main():
    mass = equation(int(input("Mass (Kg): ")))

def equation(m):
    e = m * (300000000 ** 2)
    print(e, "Joules")

main()
