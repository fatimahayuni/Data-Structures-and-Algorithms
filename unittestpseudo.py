arr = [4, 1, 2, 3, 4, 5, 6, 7, 0]

for x in range(0, len(arr)-1):
    if arr[x] < arr[x + 1]:
        print("Sorted correctly")
    else:
        print(f"Index {x} and {x+1} are sorted incorrectly")