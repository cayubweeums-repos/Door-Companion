import datetime
from time import sleep


def main():
    while True:
        now = datetime.datetime.now()
        print("Hello World, the current time is:\n\t\t\t{}:{}.{}".format(now.hour, now.minute, now.second))
        sleep(1)


main()
