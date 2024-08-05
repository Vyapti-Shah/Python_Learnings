#String Slicing - create a substring by extracting elements from another string
#               - indexing[] or slice()
#               - [start:stop:step]

name = "Bro Code"
first_name = name[:3] #0=start 3=stop
last_name = name[4:8]
funcky_name = name[0:8:2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

website1 = "https://google.com"
slice = slice(8,-4)
website2 = "https://youtube.com"
print(website1[slice])
print(website1)
print(website2[slice])
print(website2)