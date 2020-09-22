import time
import os
import sys

autv = 255
com2 = str(sys.argv[2])
temp = int(sys.argv[1])

##Mensagens de erro##
if temp < 0 and com2 == "-c":
    print("Error - can only create files with positive names , no files were created")
elif temp < 0 and com2 == "-r":
    print("Error - can only remove files with positive names , no files  were deleted")

if str(temp) == "-a" :
    if com2 == "-c" :
        while not autv < 0:
            open(str(autv),"w+")
            print("File "+str(autv)+" created")
            autv -= 1
    elif com2 == "-r" :
        while not autv < 0:
            os.remove(str(autv))
            print("File "+str(autv)+" deleted")
            autv -= 1

elif not str(temp) == "-a":
    temp = int(temp)
    if com2 == "-c" :
        while not temp < 0:
            open(str(temp),"w+")
            print("File "+str(temp)+" created")
            temp -= 1
    elif com2 == "-r" :
        while not temp < 0:
            os.remove(str(temp))
            print("File "+str(temp)+" deleted")
            temp -= 1
