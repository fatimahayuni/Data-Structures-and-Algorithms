from insertsort import *

def booleon_unittest():
    is_ordered = True

    for x in range(0, len(arr)-1):
        if arr[x] > arr[x+1]:
            is_ordered = False
            break

    if is_ordered:
        print("Correctly sorted")
    else:
        print("NOPE. Not correctly sorted.")