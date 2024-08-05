# thread - a flow execution. Like a separate order of instructions
#        - each thread takes a turn running to achieve concurrency
#        - GIL = (global onterpreter lock)
#        - allows only one thread to hold the control of the Python interpreter
# one thread runs at one time

# CPU board = program/task spends most of it's time waiting for internal events (CPU intensive) use multiprocessing
# io board = program/task spends most of it's time waiting for external events (user input, web scraping) use multithreading

import threading
import time

def breakfast():
    time.sleep(3)
    print("Ate Breakfast")
def drink_coffee():
    time.sleep(4)
    print("Drank Coffee")
def study():
    time.sleep(5)
    print("Finished Studying")

x = threading.Thread(target=breakfast,args=[])
x.start()

y = threading.Thread(target=drink_coffee,args=[])
y.start()

z = threading.Thread(target=study,args=[])
z.start()

x.join()
y.join()
z.join()

#breakfast()
#drink_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())