import time
from demos import quicksort, mergesort, bubblesort #import function from a file
import random

def create_random_list(size, max_val):
    ran_list = [ ]
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

def analyse_func(func_name, arr):
    tic = time.time()
    func_name(arr)  #Allows you to pass in function as an object
    toc = time.time()
    seconds = toc - tic # Gets you elapsed time
    print(f"{func_name.__name__.capitalize()}\t > Elapsed Time : {seconds:.5f}") #Just gives you name of function instead of string representation of object


size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
run_times = int(input("How many times do you want to run? "))
#We need to convert input from string to integer
for num in range(run_times):
    print(f"Run: {num+1}")  #So run starts at 1
    l = create_random_list(size, max)
    analyse_func(quicksort, l)
    analyse_func(mergesort, l)
    analyse_func(bubblesort, l.copy()) #So it runs on original not sorted list
    analyse_func(sorted, l)
    #Can analyse any function you want
    print("-" * 60)  #So you get a dash betwewwn each run
