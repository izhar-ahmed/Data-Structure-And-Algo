class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def print_list(self):
        if self.length == 0:
            print("Empty")
        else:
            current_node = self.first
            while current_node != None:
                print(current_node.data, end=' ')
                current_node = current_node.next
            print()
    
    def peek(self):
        if self.length == 0:
            return None
        else:
            return self.first.data
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            print("Empty")
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
        else:
            self.first = self.first.next
            self.length -= 1
        





myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(10)
myQueue.enqueue(15)
myQueue.dequeue()
myQueue.print_list( )


# print(myQueue.peek())