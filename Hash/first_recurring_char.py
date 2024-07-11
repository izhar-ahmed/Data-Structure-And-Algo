# Google question
# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# it should return 1

# My solution brute-force
def firstRecurringChar(arr):
    newArray = []
    if arr[0] == arr[1]:
            return arr[0]
    else:
        newArray.append(arr[0])
        newArray.append(arr[1])
    for i in range(2, len(arr)):
        for j in newArray:
            if arr[i] == j:
                return arr[i]
            
        newArray.append(arr[i])

# Other Solution
def firstRecurringChar2(array):
     dictionary = dict()
     for item in array:
          if item in dictionary:
               return item
          else:
               dictionary[item] = True

print(firstRecurringChar2([2,5,1,2,3,5,1,2,4]))
print(firstRecurringChar2([2,1,1,2,3,5,1,2,4]))