#Sets - collection which is unordered, unindexed. No duplicate values

utensils = {"spoon", "fork", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


#utensils.update(dishes)
#for c in utensils:
#    print(c)

#print()

#dishes.update(utensils)
#for d in dishes:
#    print(d)

#print()
print(utensils.difference(dishes)) #prints what utensils has and dishes does not

print()

print(utensils.intersection(dishes)) #prints same elements in utensils and dishes

print()

dinner_table = utensils.union(dishes)
for l in dinner_table:
    print(l)

print()

for i in utensils:
    print(i)

print()

utensils.remove("fork")
for a in utensils:
    print(a)

print()

utensils.add("napkin")
for j in utensils:
    print(j)

print()

utensils.clear()
for k in utensils:
    print(k)
