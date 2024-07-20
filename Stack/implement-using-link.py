class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_list(self):
        if self.top == None:
            print("Empty")
        else:
            current_node = self.top
            next_data = current_node.next
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next
        

    
    def peek(self):
        if self.top == None:
            return print("Empty")
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.top = new_node
            self.bottom = self.top
            self.length += 1
        else:
            holdingPointer = self.top
            self.top = new_node
            self.top.next = holdingPointer
            self.length += 1

    def pop(self):
        if self.top == None:
            self.bottom = None
            print("there is no data to pop")
        else:
            self.top = self.top.next
            self.length -= 1
    
    def isEmpty(self):
        if self.bottom == None:
            return True
        else:
            return False



myStack = Stack()
myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.pop()
myStack.pop()
myStack.pop()
myStack.print_list()
        