# 5->10->15

#Linked lists are, as the name suggests, a list which is linked.
#It consists of nodes which contain data and a pointer to the next node in the list.
#The list is connected with the help of these pointers.
#These nodes are scattered in memory, quite like the buckets in a hash table.
#The node where the list starts is called the head of theblist and the node where it ends, or last node, is called the tail of the list.
#The average time complexity of some operations invloving linked lists are as follows:
#Look-up : O(n)
#Insert : O(n)
#Delete : O(n)
#Append : O(1)
#Prepend : O(1)
#Python doesn't have a built-in implementation of linked lists, we have to build it on our own
#So, here we go.


#First we define a class Node which will act as a blueprint for each of our nodesclass Node():
class Node():
    def __init__(self, data): #When instantiating a Node, we will pass the data we want the node to hold
        self.data = data #The data passed during instantiation will be stored in self.data
        self.next = None #This self.next will act as a pointer to the next node in the list. When creating a new node, it always points to null(or None).

#Next we define the class LinkedList which will have a head pointer to point to the beginning of the list and a tail pointer to
#point to the end of the list. An optional value of length can also be stored to keep track of the length of the linked list.
#When the list is created , it is empty and there is no node to point to. So head will point to None at the time of creation of linked list
#And since the list is empty at the time of creation, we will point the tail to whatever the head is pointing to, i.e., None
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

#Next comes the append method with which we will add nodes to the end of the linked list.
#To do this, we will just pass the data we want to append. The append method will create a new instance of the Node class,
#Effectively creating a new node, with the data passed to the instance, so that the new node will contain the data the user wants to enter
#Then we will check if the list is empty. If it is, we will point the head to the new node just created and the tail to the head,
#as there is only one node in the list, so the head and tail point to the same node. Also, we will set the length equal to 1.
#If the list isn't empty, then we will make the 'next' pointer of the last node(pointed at by 'tail') point to the new node
#And update the tail to point to the new node as this has become the last node in the list now. And we'll increase the length.

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def print_list(self):
        arr = []
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        if index >= self.length:
            print("there is no such index")
        if index == 0:
            if self.head == None:
                self.head = new_node
                self.tail = self.head
                self.length += 1
            else:
                new_node.next = self.head
                self.head = new_node
                self.length += 1
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            lead_node = current_node.next
            current_node.next = lead_node.next
            self.length -= 1
        
    def reverse(self):
        # my solution: Time O(n), Space O(n)
        # link_list = []
        # rev_list = []
        # if self.length == 1:
        #     return
        # current_node = self.head
        # for i in range(self.length):
        #     link_list.append(current_node.data)
        #     current_node = current_node.next
        # i = self.length - 1
        # while i >= 0:
        #     rev_list.append(link_list[i])
        #     i -= 1
        # start_node = self.head
        # for i in range(self.length):
        #     start_node.data = rev_list[i]
        #     start_node = start_node.next
        if not self.head.next:
            return self.head
        first = self.head
        last = self.tail
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self.print_list()
        






class DNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def print_list(self):
        arr = []
        current_node = self.head
        if current_node.data == None:
            print("empty")
        while current_node != None:
            print(current_node.data, end= ' ')
            arr.append(current_node.data)
            current_node = current_node.next
        print()
        return arr
    
    def preppend(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        
    def insert(self, index, data):
        new_node = DNode(data)
        if index >= self.length:
            print("there is no such index")
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        lead_node = current_node.next
        current_node.next = new_node
        new_node.next = lead_node
        lead_node.prev = new_node
        self.length += 1
        
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            lead_node = current_node.next
            follow_node = lead_node.next
            current_node.next = follow_node
            follow_node.prev = current_node
        











myLinkedList = LinkedList()
myLinkedList.print_list()
myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.prepend(2)
myLinkedList.insert(1, 1) # [2,1,5,10]
myLinkedList.insert(3, 7) # [2,1,5,7,10]
#myLinkedList.insert(4,11) # [2,1,5,7,10,11]
myLinkedList.print_list()
print("reverse linked list")
myLinkedList.reverse()
print("-----------------------------")
myDoublyLinkList = DoublyLinkedList()
myDoublyLinkList.append(5)
myDoublyLinkList.append(10)
myDoublyLinkList.append(15)
myDoublyLinkList.preppend(2) # 2 5 10 15 
myDoublyLinkList.insert(2, 44) # 2,5,44,10,15
myDoublyLinkList.remove(2)
myDoublyLinkList.print_list()
