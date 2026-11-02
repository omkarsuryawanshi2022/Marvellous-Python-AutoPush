import psutil
import sys
import os
import time
import schedule

def PlatformServilance(FoldarName):
    Border = "_"*50
    Ret = False
    Ret = os.path.exists(FoldarName)

    if(Ret == True):
        Ret = os.path.isdir(FoldarName)
        if(Ret == False):
            print("unable to proceeed  as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FoldarName)
        print("Directory from the log file get created gets sussfully ")


    Timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FoldarName,"Marvellous_%s.log" %Timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets sucessfully created with name :{FileName}")

    fobj.write(Border+"\n")
    fobj.write("-------   marvellous plateform servilance system   -------\n")
    fobj.write("Log file gets created at " +Timestamp+"\n")
    fobj.write(Border+"\n\n")
    fobj.write("---------------- sysytem Report    -------------------\n")

    # Cpu information

    fobj.write("number of active corsin cpu :%s \n" %psutil.cpu_count())
    fobj.write("Cpu usage :%s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n")
    
    fobj.write(Border+"\n")

    # RAM Information

    Memory = psutil.virtual_memory()

    fobj.write("RAM usage :%s %%\n" %Memory.percent)

    fobj.write("Total RAM Available :%s\n" %Memory.total)

    


    fobj.write("-------------------  End of Log    -------------------\n")

    fobj.write(Border+"\n")

    fobj.close()


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

###### actutal project code

    elif(len(sys.argv) == 3):

        #print("Cpu Usage:",psutil.cpu_percent())
        print("Schedullar starter sucessfully")
        print("Press CTL + C to abort the automation script")
        #PlatformServilance(sys.argv[2])
        schedule.every(int(sys.argv[1])).minutes.do(PlatformServilance,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)
            

    else:
        print("Invalid number of argument:")
        print("unable  to processed as argument are not matching:")
        print("please use --h or --u flag for getting more getting more details")


    
    print(Border)
    print("-------   thank you for using marvellous plateform servilance system   -------")
    print(Border)
    

    

if __name__ == "__main__":
    main()

  