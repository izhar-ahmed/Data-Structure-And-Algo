# Space complexity
def booooo(n):
		for i in range(len(n)):
				print("booooo")

booooo([1, 2, 3, 4, 5]) # O(1)

def arrayOfHiNTimes(n):
		hiArr = []
		for i in range(n):
				hiArr.append("hi")

		return hiArr

res = arrayOfHiNTimes(5) # O(n)
print(res)
