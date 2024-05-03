from randomnumbers import *

arr = random_numbers_list()

def ayuni_unittest(arr):
    for x in range(0, len(arr)-1):
        if arr[x] == arr[x + 1]:
            continue
        elif arr[x] < arr [x + 1]:
            continue
        else:
            print(f"Index {x} and index {x+1} are sorted incorrectly: {arr[x]} and {arr[x+1]}.")