##########################################################
#
#   Importing Required Libraries
#
##########################################################

import sys
import os
import time
import hashlib
import smtplib
from email.message import EmailMessage

import schedule


##########################################################
#
#   Function Name : CalculateChecksum
#   Input : FileName
#   Output : Checksum
#   Description : Calculate MD5 checksum of file
#   Author : Omkar Suryawanshi
#
##########################################################

def CalculateChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

##########################################################
#
#   Function Name : FindDuplicate
#   Input : Directory Name
#   Output : Dictionary
#   Description : Find duplicate files using checksum
#   Author : Omkar Suryawanshi
#
##########################################################

def FindDuplicate(DirectoryName):

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Path is Invalid")
        return None

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return None

    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            try:

                CheckSum = CalculateChecksum(fname)

                if(CheckSum in Duplicate):
                    Duplicate[CheckSum].append(fname)
                else:
                    Duplicate[CheckSum] = [fname]

            except Exception:
                pass

    return Duplicate

##########################################################
#
#   Function Name : DeleteDuplicate
#   Input : Directory Name
#   Output : Number of deleted files
#   Description : Delete duplicate files
#   Author : Omkar Suryawanshi
#
##########################################################

def DeleteDuplicate(DirectoryName):

    MyDict = FindDuplicate(DirectoryName)

    if(MyDict == None):
        return 0, []

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    DeletedFiles = []

    for value in Result:

        for subvalue in value:

            Count = Count + 1

            if(Count > 1):

                try:

                    os.remove(subvalue)

                    DeletedFiles.append(subvalue)

                    TotalDeleted = TotalDeleted + 1

                except Exception:
                    pass

        Count = 0

    return TotalDeleted, DeletedFiles

##########################################################
#
#   Function Name : CreateLogDirectory
#   Input : Folder Name
#   Output : True / False
#   Description : Create directory for log files
#   Author : Omkar Suryawanshi
#
##########################################################

def CreateLogDirectory(FolderName):

    Ret = os.path.exists(FolderName)

    if(Ret):

        Ret = os.path.isdir(FolderName)

        if(not Ret):
            print("Unable to proceed as directory name exists but it is not a directory")
            return False

    else:

        os.mkdir(FolderName)

        print("Directory for the log file gets created successfully")

    return True

##########################################################
#
#   Function Name : CreateLogFile
#   Input : Folder Name
#   Output : Log File Name
#   Description : Create timestamp based log file
#   Author : Omkar Suryawanshi
#
##########################################################

def CreateLogFile(FolderName):

    Border = "-" * 60

    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")

    FileName = os.path.join(
        FolderName,
        "DuplicateRemovalLog_%s.log" % timestamp
    )

    fobj = open(FileName, "w")

    print("Log file gets successfully created with name :", FileName)

    fobj.write(Border + "\n")
    fobj.write("        Marvellous Duplicate File Remover\n")
    fobj.write(Border + "\n")
    fobj.write("Log File Created At : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    fobj.close()

    return FileName

##########################################################
#
#   Function Name : Marvellous_Send_mail
#   Input         : sender, app_password, receiver, subject, body
#   Output        : None
#   Description   : Sends an email via Gmail SMTP server with the provided details
#   Author        : Omkar Nanaso Suryawanshi
#
##########################################################

def Marvellous_Send_mail(sender, app_password, receiver, subject, body):
    try:
        # Create Email Object
        msg = EmailMessage()

        # Set Email Headers
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Set Email Body
        msg.set_content(body)

        print("Connecting to Gmail Server...")

        # Connect to Gmail SMTP Server
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        print("Login Successful...")

        # Login
        smtp.login(sender, app_password)

        print("Sending Mail...")

        # Send Email
        smtp.send_message(msg)

        # Close Connection
        smtp.quit()

        print("Mail sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication Failed!")
        print("Check your Gmail address and App Password.")
    except smtplib.SMTPConnectError:
        print("Unable to connect to Gmail SMTP Server.")
    except Exception as e:
        print("Error :", e)

##########################################################
#
#   Function Name : DirectoryScanner
#   Input         : DirectoryPath
#   Output        : None
#   Description   : Scans the specified directory, finds and
#                   deletes duplicate files, creates a log
#                   file, and sends the log through email.
#   Author        : Omkar Nanaso Suryawanshi
#
##########################################################

def DirectoryScanner(DirectoryPath):

     # Your scanning code

    sender = "omkar@gmail.com"
    app_password = "abcdefghijklmnop"
    receiver = "abc@gmail.com"

    subject = "Duplicate File Removal Report"

    body = "Duplicate files removed successfully."


    timestamp = time.ctime()
    logfilename   = "Marvellous%s.log"%(timestamp)

    logfilename = logfilename.replace("","_")

    logfilename = logfilename.replace(":","_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error: there is no such directory with name ",DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)  

    if(Ret == False):
        print("Marvellous Automation Error: it is not a directory with name :",DirectoryPath)
        return

    print(" log file gets created with name :",logfilename)

    fobj = open(logfilename,"w")
    
    fobj.write("marvellous automation script \n")

    fobj.write("Files from the directory are : \n")
    for Foldarname , subfoldar , filename in os .walk(DirectoryPath):
        for fname in filename:
            fobj.write(fname+"\n")

            

    fobj.close()

##########################################################
#
#   Main Function
#
##########################################################

def main():
    print("Program Started")

    Border = "-" * 60

    print(Border)
    print("      Marvellous Duplicate File Removal Automation")
    print(Border)

    if(len(sys.argv) == 3):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script removes duplicate files from a directory.")
            print("Use --u option for proper command usage.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print("python DuplicateFileRemoval.py DirectoryPath")
            print("")
            print("Example :")
            print(r'python DuplicateFileRemoval.py "E:\Data\Demo"')

        else:

            DirectoryPath = sys.argv[1]

            # Only one function call
            # Remaining functions are called internally
            #DirectoryScanner(DirectoryPath)
            
            schedule.every(int(sys.argv[1])).minutes.do(DirectoryScanner, sys.argv[2])


            while True:
                schedule.run_pending()
                time.sleep(1)

    else:

        print("Invalid number of arguments.")
        print("")
        print("Help  : python DuplicateFileRemoval.py --h")
        print("Usage : python DuplicateFileRemoval.py --u")

    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)


##########################################################
#
#   Starter
#
##########################################################

if __name__ == "__main__":
    main()



# Expected function call flow
# main()
#   │
#   ▼
# DirectoryScanner()
#   │
#   ├──► CreateLogDirectory()
#   │        │
#   │        └──► CreateLogFile()
#   │
#   ├──► DeleteDuplicate()
#   │        │
#   │        └──► FindDuplicate()
#   │                 │
#   │                 └──► CalculateChecksum()
#   │
#   └──► Marvellous_Send_mail()