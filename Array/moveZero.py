# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# my solution
def moveZero(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    
    return arr

print(moveZero([0, 1, 0, 3, 12]))

# other solution
def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z += 1
    return array
print(swap_move([0, 1, 0, 3, 12]))