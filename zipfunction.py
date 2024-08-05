# zip function - aggregate elements from two or more iterables (lists,tuples,sets,etc.)
#              - creates a zip object with paired elements stored in tuples for each element

username = ["Vyapti","Sejal","Sanjay"]
passwords = ["abc@123","cde@234","efg@456"] 

users = zip(username,passwords) #zip

print(type(users))

for i in users:
    print(i)

print()

users_list = list(zip(username,passwords)) #list

print(type(users_list))

for i in users_list:
    print(i)

print()

users_dict = dict(zip(username,passwords)) #dictionary

print(type(users_dict))

for key,value in users_dict.items():
    print(key + " : " + value)


login_date = ["13/04/2025","01/04/2024","02/01/2023"]
user = zip(username,passwords,login_date)
for i in user:
    print(i)