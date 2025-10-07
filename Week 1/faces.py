def main():
    text = convert(input("Text: "))

def convert(code):
    code = code.replace(":)", "🙂").replace(":(", "🙁")
    print(code)

main()
