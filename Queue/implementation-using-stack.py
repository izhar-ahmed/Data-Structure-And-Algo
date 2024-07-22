class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def peek(self):
        if len(self.s1) == 0:
            print("Queue is empty")
        else:
            return self.s1[0]
    
    def enqueue(self, data):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)
        return
    
    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")
        else:
            return self.s1.pop()
    
    def print_list(self):
        for i in self.s1:
            print(i, end=' ')
        print()
        

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(10)
myQueue.enqueue(15)
myQueue.print_list()
        