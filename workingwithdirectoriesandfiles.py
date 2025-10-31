#Working with path, files, and directories 
#Directories: it is a collection of files and other directories, also known as subdirectories.
#Python's os module provides functions to interact with the operating system, allowing you to work with files and directories.

#Get Current Working Directory- getcwd()
import os
print("Current Working Directory:", os.getcwd())

#Change Directory- chdir()
os.chdir('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\python')  #Change to your desired directory path
print("Directory changed successfully")

#List Files and Directories- listdir()
print("Files and Directories in 'python' folder:", os.listdir())

#Making a New Directory- mkdir()
os.chdir('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\python')
new_dir = 'NewFolder_of_mkdir' #Create a new directory(folder) named 'NewFolder_of_mkdir' 
os.mkdir(new_dir)
print(f"Directory '{new_dir}' created successfully")

#Removing a Directory- rmdir()
os.rmdir(new_dir)
print(f"Directory '{new_dir}' removed successfully")

#Rename a Directory or File- rename()
old_name = 'old_file.txt'
new_name = 'new_file.txt'
with open(old_name, 'w') as f:  #Create a file named 'old_file.txt'
    f.write("This is a sample file.")
os.rename(old_name, new_name)
print(f"File renamed from '{old_name}' to '{new_name}' successfully")