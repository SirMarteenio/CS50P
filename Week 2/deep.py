def main():
    ans = input("What is the answer to the Great Question of Life? ").strip().lower()
    if ifs(ans) is True:
        print("Yes")
    else:
        print("No")

def ifs(a):
    if a == "42" or a in ["forty-two", "forty two"]:
        return True
    else:
        return False

main()
