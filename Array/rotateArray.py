# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# My solution 1
def rotateArray(arr, k):
    for i in range(k):
        item = arr.pop()
        arr.insert(0, item)
    return arr



# My solution 2
def rotateArray2(arr, k):
    newArray = []
    j = k
    for i in range(k):
        newArray.append(arr[len(arr) - j])
        j -= 1
    print(newArray)
    for i in range(len(arr) - k):
        newArray.append(arr[i])
    
    return newArray

print(rotateArray2([1,2,3,4,5,6,7], 2))