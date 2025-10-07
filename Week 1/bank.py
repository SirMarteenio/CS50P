def main():
    greeting = input("Greeting: ").lower().strip().capitalize()
    money(greeting)

def money(a):
    if "Hello" in a:
        print("$0")
    elif "H" in a:
        print("$20")
    else:
        print("$100")

main()
