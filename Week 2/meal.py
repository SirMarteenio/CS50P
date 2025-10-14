def main():
    time = input("What time is it? ")
    convert(time)
    if 7 <= string and 8 >= string:
        print("breakfast time")
    elif 12 <= string and 13 >= string:
        print("lunch time")
    elif 18 <= string and 19 >= string:
        print("dinner time")

def convert(a):
    global string
    hour, minute = a.split(":")
    fraction = int(minute) / 60
    hour = int(hour)
    string = hour + fraction
    return(string)

main()
