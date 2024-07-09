nemo = ["nemo" for i in range(10000)]

def findNemo(nemo):
	for i in nemo:
		if i == "nemo":
			print("found nemo") # O(n) linear time -> time to execute a code increases as the input increases.

findNemo(nemo) # O(n)