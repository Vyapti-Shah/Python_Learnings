#Loop Control Statement - change a loops execution from its normal sequence 

#break - used to terminate the loop entirely
#continue - skips to the next iteration of the loop
#pass - does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break
print("Hello " + name)

print()

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print()

for j in range(1,21):
    if j == 17:  #skips 17 while printing
        pass
    else:
        print(j)