# Given 2 arrays, Create a function that lets user know (true / false)
# whether these two array contain any common items	
# for example:
# array1 = ["a", "b", "c", "x"]
# array2 = ["z", "y", "i"]
# should return false
# array1 = ["a", "b", "c", "x"]
# array2 = ["a", "z", "y", "i"]
# should return true

# def commonElement(arr1, arr2):
# 		for i in arr1:
# 				for j in arr2:
# 						if i == j:       # O(n^2)
# 								return True  
# 						else:
# 								return False
						
# print(commonElement([1, 3, 4, 5], [3, 6, 7, 8]))

# time complexity is O(n^2)

# first we convert first array to object.
# then we loop through second array to check element in second array is in object or not.
# then we return true or false accordingly.

def commonElement2(arr1, arr2):
		obj = {}
		for i in arr1:
				obj.update({i : i})
		
		for i in arr2:
				if i in obj:
						return True
		return False
print(commonElement2([1,2,3,4], [5,1,6,8]))

# O(a + b)




