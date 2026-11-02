# python processsurvilance.py 2 marvellous.log
# python processsurvilance  time_interval  foldar_name
#              0                 1            2
#  len(sys.argv) ->  3

import psutil
import sys
import os


def main():
    Border = "_"*50
    print(Border)
    print("-------   marvellous plateform servilance system   -------")
    print(Border)

# -- h and  --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or  sys.argv[1] == "--H"):
            print("this automation  script isused to perform:")
            print("1 :  it fetch the information for running process")
            print("2 it fetch informastion about primary storage as a the RAM")
            print("3 it fetch informastion about Secondary storage as a HDD")
            print("4 it fetch informastion about Microprocesser")
            print("5 it gets auto shedule peridicollay")
            print("6 it maintain into all record into log file")
            print("7 it send mail peridically")

        elif(sys.argv[1] == "--u" or  sys.argv[1] == "--U"):
            print("use the automation script as :")
            print(f"python {sys.argv[0]} time_interval foldar_name")
            print("time_interval : time in  minute for peridoic excecution")
            print("foldar_name : name of foldar for the log file creation")
        else:
            print("unable tp process as there is no matching argument")
            print("please use --h or --u flag for getting more getting more details")

# actutal project code
    elif(len(sys.argv) == 3):
        pass

    else:
        print("Invalid number of argument:")
        print("unable  to processed as argument are not matching:")
        print("please use --h or --u flag for getting more getting more details")


    
    print(Border)
    print("-------   thank you for using marvellous plateform servilance system   -------")
    print(Border)
    

    

if __name__ == "__main__":
    main()

  