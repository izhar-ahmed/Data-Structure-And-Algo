def selectionSort(arr):
    for i in range(len(arr)):
        position = 0
        smallElement = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < smallElement:
                smallElement = arr[j]
                position = j
        if smallElement == arr[i]: 
            arr[i] = smallElement
        else:
            arr[position] = arr[i]
            arr[i] = smallElement
    return arr

number = [64, 25, 12, 22, 11]
print(selectionSort(number))

#[11,12,22,25,64]
        