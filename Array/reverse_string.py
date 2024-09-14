# create a function that reverse a string:
# "Hi my name is izhar" should be
# "rahzi si eman ym ih"

def reverse_string(str):
		rev_str = ""
		for i in range(len(str)-1, -1, -1):
				rev_str += str[i]
		
		return rev_str

def reverse_string2(s): # Time O(n) Space O(1)
	s = list(s)
	l, r = 0, len(s) - 1
	while l < r:
		s[l] = s[r]
		s[r] = s[l]
		l += 1
		r -= 1

# Using stack
def reverse_string3(s): # Time O(n) Space O(n)
	s = list(s)
	stack = []
	for c in s:
		stack.append(c)
	i = 0
	while stack:
		s[i] = stack.pop()
		i += 1
	return s

# Using recursive
def reverse_string4(s):
	s = list(s)
	def recursive(l, r):
		if l < r:
			s[l], s[r] = s[r], s[l]
			recursive(l + 1, r - 1)
	recursive(0, len(s) - 1)
	return s

print(reverse_string4("hello"))


