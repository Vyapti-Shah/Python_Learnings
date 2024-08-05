# file detection # os = operating system
import os

path_loc = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt" # \\ because thats the escape sequence for a string

if os.path.exists(path_loc):
    print("The location exisits!")
    if os.path.isfile(path_loc):
        print("It is a file")
    elif os.path.isdir(path_loc):
        print("It is a folder")
else:
    print("The location does not exisit!")

print()

path_loc_1 = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\file.py" 

if os.path.exists(path_loc_1):
    print("The location exisits!")
    if os.path.isfile(path_loc_1):
        print("It is a file")
    elif os.path.isdir(path_loc_1):
        print("It is a folder")
else:
    print("The location does not exisit!")