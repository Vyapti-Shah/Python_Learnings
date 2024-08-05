# sort() method - used with lists
# sort() function - used with iterables

people = ["Vyapti","Sejal","Sanjay","Jiya","Jinit"]
people.sort()   #sort method
for i in people:
    print(i)

print()

people.sort(reverse=True)  #sort method
for j in people:
    print(j)

print()

fruits = ["Muskmelon","Apple","Mango","Pear","Wtermelon"]
sorted_fruits = sorted(fruits) #sorted function
for i in sorted_fruits:
    print(i)

print()

sorted_fruits = sorted(fruits,reverse=True) #sorted function
for j in sorted_fruits:
    print(j)

names = [("Vyapti","A",19),
         ("Sejal","C",20),
         ("Sanjay","D",21),
         ("Jiya","A",15),
         ("Jinit","B",10)]
grade = lambda grades:grades[1]
names.sort(key=grade) #sorted method
for i in names:
    print(i)

print()

age = lambda grades:grades[1]
age = lambda ages:ages[2]
names.sort(key=age,reverse=True) #sorted method
for i in names:
    print(i)

print()

nam = lambda nams:nams[0]
sorted_nams = sorted(names,key=nam) #sorted function
for i in sorted_nams:
    print(i)