def quickSort(array, left, right):
    if left < right:
        pivot = right
        partitionIndex = partition(array, pivot, left, right)
        # sort left and right
        quickSort(array, left, partitionIndex - 1)
        quickSort(array, partitionIndex + 1, right)
    return array

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left
    for i in range(left, right):
        if array[i] < pivotValue:
            swap(array, i, partitionIndex)
            partitionIndex += 1
    swap(array, right, partitionIndex)
    return partitionIndex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

number = [3,6,8,10,1,2,1]
print(quickSort(number, 0, len(number)-1))

# Code Overview
# quickSort function: This function is the main recursive function that divides the array into smaller sub-arrays and sorts them using the partitioning process.
# partition function: This function handles the process of finding the correct position of the pivot element in the array, ensuring that all elements less than the pivot are on its left and all elements greater than the pivot are on its right.
# swap function: This is a utility function that swaps two elements in the array.
# Initial Call
# The first call is:

# python
# Copy code
# quickSort(number, 0, len(number) - 1)
# This is equivalent to:

# python
# Copy code
# quickSort([3, 6, 8, 10, 1, 2, 1], 0, 6)
# array = [3, 6, 8, 10, 1, 2, 1]
# left = 0
# right = 6
# First Call to quickSort
# left < right is true (0 < 6), so we proceed.
# pivot = right = 6, so pivotValue = array[6] = 1.
# Now, we call the partition function:
# python
# Copy code
# partition([3, 6, 8, 10, 1, 2, 1], 6, 0, 6)
# First Call to partition
# pivotValue = array[6] = 1
# partitionIndex = left = 0
# Loop through the array:
# i = 0: array[i] = 3 (not less than 1, so no swap)
# i = 1: array[i] = 6 (not less than 1, so no swap)
# i = 2: array[i] = 8 (not less than 1, so no swap)
# i = 3: array[i] = 10 (not less than 1, so no swap)
# i = 4: array[i] = 1 (equal to pivotValue, so no swap)
# i = 5: array[i] = 2 (not less than 1, so no swap)
# After the loop, partitionIndex is still 0. Now, we swap:

# python
# Copy code
# swap(array, 6, 0)
# This swaps the pivot 1 with 3:

# Array after swap: [1, 6, 8, 10, 1, 2, 3]
# The partitionIndex returned is 0.
# Back to quickSort
# The array is now [1, 6, 8, 10, 1, 2, 3].

# We make two recursive calls:
# python
# Copy code
# quickSort([1, 6, 8, 10, 1, 2, 3], 0, -1)
# This call ends immediately because left < right is false (0 < -1 is false).
# python
# Copy code
# quickSort([1, 6, 8, 10, 1, 2, 3], 1, 6)
# Now, we proceed with the right sub-array [6, 8, 10, 1, 2, 3].
# Second Call to quickSort
# pivot = right = 6, so pivotValue = array[6] = 3.
# Call to partition:
# python
# Copy code
# partition([1, 6, 8, 10, 1, 2, 3], 6, 1, 6)
# Second Call to partition
# pivotValue = 3
# partitionIndex = 1
# Loop through the array:
# i = 1: array[i] = 6 (not less than 3, so no swap)
# i = 2: array[i] = 8 (not less than 3, so no swap)
# i = 3: array[i] = 10 (not less than 3, so no swap)
# i = 4: array[i] = 1 (less than 3, so swap with partitionIndex = 1):
# Swap 6 with 1: [1, 1, 8, 10, 6, 2, 3]
# partitionIndex = 2
# i = 5: array[i] = 2 (less than 3, so swap with partitionIndex = 2):
# Swap 8 with 2: [1, 1, 2, 10, 6, 8, 3]
# partitionIndex = 3
# After the loop, swap the pivot with the element at partitionIndex:

# Swap 10 with 3: [1, 1, 2, 3, 6, 8, 10]
# partitionIndex returned is 3.
# Recursion Continues
# The array is now [1, 1, 2, 3, 6, 8, 10].

# Recursive calls:
# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 1, 2)
# Handles the sub-array [1, 2] with pivot 2.
# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 4, 6)
# Handles the sub-array [6, 8, 10] with pivot 10.
# These sub-arrays will be sorted individually, but since they're already almost sorted, the partition will quickly finish, and the full array [1, 1, 2, 3, 6, 8, 10] will be the final sorted array.

# Handling the Sub-array [1, 2] with Pivot 2
# When the quickSort function is called on the sub-array [1, 2], here's what happens:

# Initial Call:

# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 1, 2)
# Here, left = 1 and right = 2, so the sub-array being considered is [1, 2].
# pivot = right = 2, so pivotValue = array[2] = 2.
# Partitioning:

# The partition function is called:
# python
# Copy code
# partition([1, 1, 2, 3, 6, 8, 10], 2, 1, 2)
# partitionIndex starts at left = 1.
# Now, the loop iterates over the sub-array [1, 2]:
# i = 1: array[i] = 1 (which is less than 2), so swap array[1] with array[partitionIndex]. Since they're the same, the array remains [1, 1, 2, 3, 6, 8, 10], and partitionIndex increases to 2.
# After the loop, the pivot 2 is already at its correct position, so no swap is needed.
# Recursive Calls:

# The quickSort function is called on the two new sub-arrays:
# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 1, 1)  # Left side of pivot
# quickSort([1, 1, 2, 3, 6, 8, 10], 3, 2)  # Right side of pivot
# Both calls immediately return because left is not less than right (1 is not less than 1, and 3 is not less than 2).
# Result: The sub-array [1, 2] is already sorted.

# Handling the Sub-array [6, 8, 10] with Pivot 10
# Now, let's see how the quickSort function handles the sub-array [6, 8, 10]:

# Initial Call:

# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 4, 6)
# Here, left = 4 and right = 6, so the sub-array being considered is [6, 8, 10].
# pivot = right = 6, so pivotValue = array[6] = 10.
# Partitioning:

# The partition function is called:
# python
# Copy code
# partition([1, 1, 2, 3, 6, 8, 10], 6, 4, 6)
# partitionIndex starts at left = 4.
# Now, the loop iterates over the sub-array [6, 8, 10]:
# i = 4: array[i] = 6 (which is less than 10), so swap array[4] with array[partitionIndex]. Since they're the same, the array remains [1, 1, 2, 3, 6, 8, 10], and partitionIndex increases to 5.
# i = 5: array[i] = 8 (which is less than 10), so swap array[5] with array[partitionIndex]. Since they're the same, the array remains [1, 1, 2, 3, 6, 8, 10], and partitionIndex increases to 6.
# After the loop, the pivot 10 is already at its correct position, so no swap is needed.
# Recursive Calls:

# The quickSort function is called on the two new sub-arrays:
# python
# Copy code
# quickSort([1, 1, 2, 3, 6, 8, 10], 4, 5)  # Left side of pivot
# quickSort([1, 1, 2, 3, 6, 8, 10], 7, 6)  # Right side of pivot
# The first call sorts [6, 8], and the second call returns immediately because left is not less than right.
# Result: The sub-array [6, 8, 10] is now sorted.

# Summary
# Sub-array [1, 2]: The pivot 2 was already in its correct position, so no further sorting was needed.
# Sub-array [6, 8, 10]: The pivot 10 was already in its correct position, so it remained unchanged, and the sub-array [6, 8] was sorted.