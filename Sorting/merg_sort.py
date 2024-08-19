def mergSort(arr):
    print('Current Array: ', arr)
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
        # recursion
        mergSort(left_arr)
        mergSort(right_arr)
        # print('AFTER: left arr: ', left_arr, ' right arr: ', right_arr)
        # print('AFTER: Current Array: ', arr)
        # print('---')

        # merg
        i = 0 # left arr indx
        j = 0 # right arr indx
        k = 0 # merged arr indx
        # print(arr)
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    print('Result: ', arr)
    


mergSort([6,5,3,1,8,7,2,4])

# Continuing with mergSort([6,5,3,1,8,7,2,4])
# 1. Initial Call: mergSort([6,5,3,1,8,7,2,4])
# The function prints Current Array: [6, 5, 3, 1, 8, 7, 2, 4].
# It checks if the length of the array (8) is greater than 1. Since it is, the array is divided into two halves:
# left_arr = [6, 5, 3, 1]
# right_arr = [8, 7, 2, 4]
# The function then calls mergSort([6,5,3,1]) to sort the left half.
# 2. Recursive Call: mergSort([6,5,3,1])
# The function prints Current Array: [6, 5, 3, 1].
# It checks if the length of the array (4) is greater than 1. Since it is, the array is divided into two halves:
# left_arr = [6, 5]
# right_arr = [3, 1]
# The function then calls mergSort([6,5]) to sort the left half of this split.
# 3. Recursive Call: mergSort([6,5])
# The function prints Current Array: [6, 5].
# It checks if the length of the array (2) is greater than 1. Since it is, the array is divided into two halves:
# left_arr = [6]
# right_arr = [5]
# The function then calls mergSort([6]).
# 4. Base Case: mergSort([6])
# The function prints Current Array: [6].
# It checks if the length of the array (1) is greater than 1. Since it's not (because 1 is not greater than 1), the function stops here and returns, meaning no further splitting or merging happens with [6].
# 5. Back to mergSort([6,5]), Now Handling mergSort([5])
# The function continues where it left off in the previous call.
# It now calls mergSort([5]).
# 6. Base Case: mergSort([5])
# The function prints Current Array: [5].
# It checks if the length of the array (1) is greater than 1. Since it’s not, the function stops here and returns.
# 7. Merging [6] and [5]
# Now the function begins the merge process for [6] and [5] in the mergSort([6,5]) call:
# It initializes indices i = 0, j = 0, and k = 0 to track positions in left_arr, right_arr, and the original array arr.
# It compares left_arr[i] (which is 6) with right_arr[j] (which is 5).
# Since 5 is smaller, it places 5 in the first position of the original array: arr[k] = 5. Now arr is [5, 5].
# It increments j and k by 1 (j = 1, k = 1).
# Now, since there are no more elements in right_arr (j has exceeded its length), the remaining element from left_arr (6) is placed in the original array: arr[k] = 6.
# The array is now [5, 6].
# 8. Back to mergSort([6,5,3,1]), Now Handling mergSort([3,1])
# After merging [6] and [5] into [5, 6], the function returns to where it left off in mergSort([6,5,3,1]).
# It now calls mergSort([3,1]).
# 9. Recursive Call: mergSort([3,1])
# The function prints Current Array: [3, 1].
# It checks if the length of the array (2) is greater than 1. Since it is, the array is divided into two halves:
# left_arr = [3]
# right_arr = [1]
# The function then calls mergSort([3]).
# 10. Base Case: mergSort([3])
# The function prints Current Array: [3].
# It checks if the length of the array (1) is greater than 1. Since it’s not, the function stops here and returns.
# 11. Back to mergSort([3,1]), Now Handling mergSort([1])
# The function continues where it left off and now calls mergSort([1]).
# 12. Base Case: mergSort([1])
# The function prints Current Array: [1].
# It checks if the length of the array (1) is greater than 1. Since it’s not, the function stops here and returns.
# 13. Merging [3] and [1]
# Now the function begins the merge process for [3] and [1] in the mergSort([3,1]) call:
# It initializes indices i = 0, j = 0, and k = 0.
# It compares left_arr[i] (3) with right_arr[j] (1).
# Since 1 is smaller, it places 1 in the first position of the original array: arr[k] = 1. Now arr is [1, 1].
# It increments j and k by 1.
# Now, since there are no more elements in right_arr, the remaining element from left_arr (3) is placed in the original array: arr[k] = 3.
# The array is now [1, 3].
# 14. Merging [5, 6] and [1, 3]
# After merging [5, 6] and [1, 3], the function returns to where it left off in mergSort([6,5,3,1]).
# It starts merging [5, 6] and [1, 3]:
# It initializes i = 0, j = 0, and k = 0.
# It compares left_arr[i] (5) with right_arr[j] (1).
# Since 1 is smaller, it places 1 in the original array: arr[k] = 1. Now arr is [1, 5, 3, 1].
# It increments j and k by 1.
# It compares left_arr[i] (5) with right_arr[j] (3).
# Since 3 is smaller, it places 3 in the original array: arr[k] = 3. Now arr is [1, 3, 3, 1].
# It increments j and k by 1.
# Now, since there are no more elements in right_arr, the remaining elements from left_arr (5 and 6) are placed in the original array: arr[k] = 5, then arr[k] = 6.
# The array is now [1, 3, 5, 6].
# 15. Back to the Original Call, Now Handling mergSort([8,7,2,4])
# The function returns to the original call mergSort([6,5,3,1,8,7,2,4]) and now handles the right half, mergSort([8,7,2,4]).
# And the process continues in the same way for the right half, recursively splitting and then merging until the entire array is sorted.

# By the end, [1, 3, 5, 6] and [2, 4, 7, 8] are merged together to form the final sorted array [1, 2, 3, 4, 5, 6, 7, 8].
