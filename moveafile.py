#move a file
import os
source = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test3.txt"
destination = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test3_moved.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found!")

#test3.txt got deleted and moved to test3_moved.txt 