#delete a file
import os
import shutil 

path = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test4.txt"

try:
    os.remove(path) #method used to delete files
except FileNotFoundError:
    print("The file was not found")
else:
    print("The file is deleted")

#It deleted the test4.txt file

print()

path_empty = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test4_emptyfolder"

try:
    os.remove(path_empty) #method used to delete files
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete")

print()

path_empty_0 = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test4_emptyfolder_0"

try:
    #os.remove(path_empty) # method used to delete files
    os.rmdir(path_empty_0) #method used to delete empty folders
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete")
else:
    print("The folder is deleted")

#It deleted the test4_empty folder

print()

path_notempty = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test4_notemptyfolder"

try:
    #os.remove(path_empty) # method used to delete files
    os.rmdir(path_notempty) #method used to delete empty folders
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete")
except OSError:
    print("You cannot delete it using that funciton")
else:
    print("The folder is deleted")

print()


path_notempty_0 = "C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test4_notemptyfolder_0"

try:
    #os.remove(path_empty) # method used to delete files
    #os.rmdir(path_empty_0) #method used to delete empty folders
    shutil.rmtree(path_notempty_0) #method used to delete folders filled with files (ie not empty folders)
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete")
except OSError:
    print("You cannot delete it using that function")
else:
    print("The folder is deleted")

#It deleted the test4_notemptyfolder_0 folder