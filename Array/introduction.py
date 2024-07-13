#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
#In Python we only have dynamic arrays
#Some basic operations and their complexities are given below :

#Look-up/Accses - O(1)
#Push/Pop - O(1)*
#Insert - O(n)
#Delete - O(n)

array = ["a", "b", "c", "d"]
# 4 x 4 = 16 Byte

# access/lookup
print(array[0]) # a O(1)

# append
array.append("e") # O(1)
print(array)

# pop
array.pop() # O(1)
print(array)

# insert
#Insert operation inserts an element at the beginning of the array, or at any location specified.
#This is O(n) operation since after inserting the element at the desired location,
#The elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
#This requires looping through the array. Hence, O(n) time.
array.insert(0, "z") # O(n)
print(array)

#Delete
#Similar to insert, it deletes an element from the specified location in O(n) time
#The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
#Hence, O(n) time complexity
array.pop(0) # O(n)
print(array)

array.remove("b") # O(n) because it shift index of all element
print(array)

