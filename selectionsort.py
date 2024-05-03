from randomnumbers import random_numbers_list
from ayuni_unittest import *
import time

# Start timer
start_time = time.time()

arr = random_numbers_list()

n = len(arr)

def selectionsort(arr):
   for a in range(0, n-1):
      current_min_index = a

      for b in range(a + 1, n):
         if arr[current_min_index] >= arr[b]:
            current_min_index = b

      arr[a], arr[current_min_index] = arr[current_min_index], arr[a]
   print(arr)

selectionsort(arr)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time for insert sort: ", elapsed_time) 
# ayuni_unittest(arr)
