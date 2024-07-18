#Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.
#Here, we will implement our own array with some common methods such as access, push, pop, insert, delete

class Myarray():
		def __init__(self):
				self.length = 0
				self.data = {}

		def __str__(self): # used to define string representation of object
				return str(self.__dict__)
		
		def get(index, self):
				return self.data[index]
		
		def push(self, item):
				self.length += 1
				self.data[self.length - 1] = item
				return self.length
		
		def pop(self): 
				last_item = self.data[self.length -1]
				del self.data[self.length - 1] # del 
				self.length -= 1
				return last_item
		
		def dele(self, index):
				for i in range(index, self.length - 1):
						self.data[i] = self.data[i + 1]
				del self.data[self.length - 1]
				self.length -= 1


arr = Myarray()

arr.push("a")
arr.push("b")
arr.push("c")
arr.push("d")

arr.pop()

arr.dele(1)
arr.push("izhar")
arr.dele(2)
print(arr)

		