def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # Swap numbers
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

number = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubbleSort(number)) # O(n ^ 2)
