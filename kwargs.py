# **kwargs - parameter that will pick all arguements into a dictionary
#          - useful so that a function can accept a varying amount of keyword arguements 

def hello(**stuff):
    print("Hello " + stuff['first'] + " " + stuff['last']) #output = Hello Vyapti Shah
    print("Hello",end=" ")
    for key,value in stuff.items():
        print(value,end=" ")

hello(title="Miss",first="Vyapti",middle="Sanjay",last="Shah")