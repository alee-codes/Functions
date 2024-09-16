def main(time):
    time = input("Enter time: ")

if 7 <= hours <= 8 and 0 <= minutes <= 60:
    print("Breakfast Time")

elif 12 <= hours <= 13 and 0 <= minutes <= 60:
    print("Lunch Time")

elif 18 <= hours <= 19 and 0 <= minutes <= 60:
    print("Dinner Time")

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = float(minutes) / 60
    converted_time = convert(time)
    return hours + minutes

if __name__ == "__main__":

    main()
