from randomnumbers import random_numbers_list
from ayuni_unittest import *
import time

# Start timer
start_time = time.time()

arr = random_numbers_list()

def insertsort(arr):

    for a in range(1, len(arr)):
        b = a
        # while b is more or equal to 0 AND arr[b] is less than arr[b-1], 
        while arr[b] < arr[b-1] and b >= 0 and (b-1) >= 0:
            arr[b], arr[b-1] = arr[b-1], arr[b]
            b -= 1
    print(arr)

insertsort(arr)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time for insert sort: ", elapsed_time) 

# ayuni_unittest(arr)









    

