import time


def countdown(t):
    while t > 0:
        print(f"{t} seconds remaining")
        time.sleep(1)
        t -= 1

    print("Done")


def main():
    time_to_countdown = int(input("Enter the time to count down from in seconds: "))
    countdown(time_to_countdown)


main()
