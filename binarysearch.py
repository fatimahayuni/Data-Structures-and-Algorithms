"""
Binary Search. Only works on sorted arrays. Lets say we have an array from 1-50. We are looking for 13. We look for the index of the middle number (len(arr)/2). We then perform a check if the value of that index is bigger or smaller than 13. 25 is bigger than 13 so the second half of the array will be eliminated. We can't eliminate the actual half of the arrays so we need to mark the other half as sorted. So the length of the inner for loop will be changed to half.
Now we do another iteration of the first half of the array. We search for the middle index. len/arr divided by 4 (from the original length of the array).
Half of that would be 12.5. There's no index 12.5. So this program also needs to take into account if this array is even or odd numbers. If even numbers, we will take the earlier number. If it's index 12.5, we will take index 12.
So the code needs to take into account first if this array is odd or even numbers.
And then do the code for finding the middle index of the array.
Do the code to compare the value of that middle index.
Do the code to find the value of the middle index.
Do the code to compare the value of the middle index with the target value.
Do the code to ignore the half that's not necessary anymore. We consider this 'sorted'. This code is inside the nested for loop. Once we have ignored the unnecessary half of the array, the nested for loop ends.
Now we to back to the outer for loop and repeat the process again.
Oh wow. I am surprised with how I am tackling this new problem.
My brain can see the pattern in nested for loops and I plan my code based on the visualisation first.
It's only been 3 algorithms. I could have never done this 2 years ago. 
"""