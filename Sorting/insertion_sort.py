def insertionSort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        for j in range(i - 1, -1, -1):
            if element < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = element
                print(arr)
    return arr


number = [5,2,9,1,5,6]
print(insertionSort(number)) # O(n^2)