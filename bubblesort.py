from randomnumbers import random_numbers_list
from ayuni_unittest import *
import time

# Start timer
start_time = time.time()

arr = random_numbers_list()

n = len(arr)

def bubble_sort(arr):
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[1+j]:
                arr[j], arr[1+j] = arr[1+j], arr[j]
    print(arr)
    return arr

bubble_sort(arr)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time for bubble sort: ", elapsed_time) 




# ayuni_unittest(arr)
