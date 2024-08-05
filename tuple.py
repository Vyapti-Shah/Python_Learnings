#Tuple - collections which is ordered and unchangeable used to group together related data

student = ("Vyapti",19,"female")
print(student.count("Vyapti"))
print(student.index("female"))

print()

for i in student:
    print(i)

print()

if "Vyapti" in student:
    print("Vyapti is here!")