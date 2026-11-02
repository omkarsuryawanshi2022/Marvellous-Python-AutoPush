import schedule
import time
import datetime
def display():
    print("Gay ganesh...",datetime.datetime.now())
def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(display)
    # Issue

if __name__ == "__main__":
    main()

   