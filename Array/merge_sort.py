# my solution
def merg_sort(arr1, arr2):
		newArray = []
		for i in arr1:
				for j in arr2:
						if i < j:
								if arr1[len(arr1) - 1] == i and arr2[len(arr2) - 1] == j:
										newArray.append(i)
										newArray.append(j)
								else:
										newArray.append(i)
										break
						elif i > j:
								if arr1[len(arr1) - 1] == i and arr2[len(arr2) - 1] == j:
										newArray.append(j)
										newArray.append(i)
								else:
										newArray.append(j)
						elif i == j:
								newArray.append(i)
								break
		return newArray

# Second solution
def merg_sort2(arr1, arr2):
		first_array_index = 0
		second_array_index = 0
		newArray = []
		flag = 0

		while not (first_array_index >= len(arr1) or second_array_index >= len(arr2)):
				if arr1[first_array_index] <= arr2[second_array_index]:
						newArray.append(arr1[first_array_index])
						first_array_index += 1
				else:
						newArray.append(arr2[second_array_index])
						second_array_index += 1
				
				if first_array_index == len(arr1):
						flag = 1
					
		if flag == 1:
				for item in arr2[second_array_index:]:
						newArray.append(item)
		else:
				for item in arr1[first_array_index:]:
						newArray.append(item)

		return newArray

print(merg_sort2([0, 3, 4, 31], [4, 6, 30]))


