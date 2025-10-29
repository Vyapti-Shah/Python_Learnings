#There arer 2 scopes : local and global
#Local scope : used only inside a function
#Global scope : can be used inside as well as outside the function
glob = "globally available"
def f1():
    loc = "locally available"
    print(loc)
    print(glob)
f1()
print(glob)
#print(loc) #gives error because loc is local scope

print()

a = 10
def f2():
    a = 5  #local scope
    print("inside f2:",a)
f2()
print("outside f2:",a)