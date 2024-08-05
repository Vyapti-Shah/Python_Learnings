#read a file

with open('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test.txt') as file:
    print(file.read())

print(file.closed)

print()

try:
    with open('C:\\Users\\vyapti shah\\OneDrive\\Desktop\\OM\\text.txt\\test.t') as file:
        print(file.read())
except FileNotFoundError:
    print("This file cannot be found!")