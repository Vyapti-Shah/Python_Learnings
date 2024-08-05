# multiprocessing - running tasks in parallel in different cpu cores, bypasses GIL used for threa
#                 - multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                 - multithreading = better for io bound tasks (waiting around)
# as this pc has 8 processors so you can undergo 8 processes at a time and the other processes will be carried out differently
# task manager >> performance 

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0 
    while count < num:
        count += 1

def main():
    print(cpu_count())
    
    a = Process(target=counter, args=(2500,))
    b = Process(target=counter, args=(2500,))
    c = Process(target=counter, args=(2500,))
    d = Process(target=counter, args=(2500,))

    a.start()
    b.start()
    c.start()
    d.start()


    a.join() #the main function will wait for the child function to finish first 
    b.join()
    c.join()
    d.join()

    print("finished in: ",time.perf_counter(),"seconds")

if __name__ == '__main__':
    main()