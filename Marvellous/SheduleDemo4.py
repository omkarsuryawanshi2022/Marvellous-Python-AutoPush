import schedule
import time
import datetime
def display():
    print("Gay ganesh...",datetime.datetime.now())
def main():
    print("Automation Script Started")

    schedule.every(10).second.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End of Automation Script...")
    

if __name__ == "__main__":
    main()

   