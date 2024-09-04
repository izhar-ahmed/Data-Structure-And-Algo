def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # Swap numbers
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

number = [5,3,8,4,2]
print(bubbleSort(number)) # O(n ^ 2)
