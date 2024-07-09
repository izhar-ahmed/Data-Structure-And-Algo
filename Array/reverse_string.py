# create a function that reverse a string:
# "Hi my name is izhar" should be
# "rahzi si eman ym ih"

def reverse_string(str):
		rev_str = ""
		for i in range(len(str)-1, -1, -1):
				rev_str += str[i]
		
		return rev_str

print(reverse_string("izhar")) # O(n)
