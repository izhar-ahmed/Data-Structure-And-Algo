# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# My solution
def sumOfTwo(arr, target):
		i = 0
		j = 1
		while i <= len(arr):
				if j == len(arr):
						i += 1
						j = i + 1
						continue
				
				if arr[i] + arr[j] == target:
						print(f"[{i}, {j}]")
						break

sumOfTwo([3,3], 6)
