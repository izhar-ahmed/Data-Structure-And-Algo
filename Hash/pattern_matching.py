# Given 2 arrays, create a function that lets a user know (true/false) whether these two arrays contain any common items
# For example:
#  array1 = ["a", "c", "d", "x"]
# array2 = ["z", "y", "i"]
# should return false
# ------------
#  array1 = ["a", "c", "d", "x"]
# array2 = ["z", "y", "i", "x"]
# should return true

# My solution
def matchPattern(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                return True
    return False

# print(matchPattern(["a", "b", "c", "x"], ["z", "y", "x"])) # O(n * m) quadratic time

# efficient solution
def matchPattern2(arr1, arr2):
    dictionary = dict()
    for item in arr2:
        dictionary[item] = item
    for i in arr1:
        if i in dictionary:
            return True
    return False

print(matchPattern2(["a", "b", "c", "x"], ["z", "y", "x"])) # O(n + m) linear time

