# write a file 
text = "Yooooo\nThis is some written text"
text = "Uh ho this text is overwritten\n"
with open('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test1.txt','w') as file: #'w' is used for write and 'r' is used to read
    file.write(text)

text = "Have a nice day! See you!"
with open('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test1.txt','a') as file: #'a' is used for append
    file.write(text)

#go to text.txt>>test1.txt for output