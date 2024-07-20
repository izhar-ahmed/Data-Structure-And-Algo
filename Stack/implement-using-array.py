class MyStack():
    def __init__(self):
        self.array = []

    def print_stack(self):
        if len(self.array) == 0:
            print("Empty")
        else:
            for i in range(len(self.array) - 1, -1, -1):
                print(self.array[i])
    
    def peek(self):
        return self.array[len(self.array) - 1]
    
    def push(self, data):
        self.array.append(data)
    
    def pop(self):
        self.array.pop()

    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else: 
            return False


myStack = MyStack()
myStack.push("google")
myStack.push("Udemy")
myStack.push("Discort")
myStack.pop()
myStack.print_stack()




