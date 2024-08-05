# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory (ie. folder)
# copy2() = copy() + copies metadata (file's creation and modification time)

import shutil

shutil.copyfile('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2.txt','C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2_copyfile.txt') #src,dst

shutil.copy('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2.txt','C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2_copy.txt') #src,dst

shutil.copy2('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2.txt','C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test2_copy2.txt') #src,dst