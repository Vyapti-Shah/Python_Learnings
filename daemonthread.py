# daemon thread - a thread that runs in the background, not important for program to run
#               - your program will not wait for deemon threads to complete before exixting
#               - non-deemon threads cannot normally be killed, stay alive untill task is complete
#               - ex. background tasks, garbage collection, waiting for unput, long running process

import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count,"seconds")

x = threading.Thread(target=timer, daemon=True)

x.setDaemon(True)
print(x.isDaemon())

x.start()

answer = input("Do you wish to exit? \n")