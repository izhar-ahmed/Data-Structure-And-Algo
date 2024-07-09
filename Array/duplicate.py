# My solution
def duplicate(arr):
    i = 0
    j = 1

    while i <= len(arr):
        if j < len(arr):
            if arr[i] != arr[j]:
                j += 1
            else:
                return True
        else:
            i += 1
            j = i + 1
        
    return False
        
print(duplicate([1, 2, 3, 4]))

# My solution

def duplicate2(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i + 1]:
            return True
        else:
            return False
        