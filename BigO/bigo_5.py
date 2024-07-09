# arr = [1, 2, 3, 4, 5]

# def pairsOfArr(arr):
# 		print("These are all the numbers")
# 		for i in arr:
# 				print(i)
		
# 		print("these are sum of all pairs")
# 	  for i in arr:
# 				for j in arr:
# 		    		print(i + j)

# pairsOfArr(arr)

arr = [1, 2, 3, 4, 5]

def pairsOfArr(arr):
    print("These are all the numbers")
    for i in arr:
        print(i)
    
    print("These are the sums of all pairs")
    for i in arr:
        for j in arr:
            print(i + j)

pairsOfArr(arr)