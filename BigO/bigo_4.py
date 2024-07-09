arr = [1, 2, 3, 4, 5]

def pairsOfArr(arr):
	for i in arr:
		for j in arr:
			print(f"({i}, {j})")

pairsOfArr(arr)

# O(n ^ 2)