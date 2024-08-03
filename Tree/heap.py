# A heap is a tree where every parent is gretaer than its children ( for max-heaps ) or they are smaller than their children ( for min-heaps)
#A Max heap( and min heap) is typically represented as an array. The root element will be at Arr[0]. Arr[(i-1)/2] Returns the parent node.
#Arr[(2*i)+1] Returns the left child node. Arr[(2*i)+2] Returns the right child node. Operations on Max Heap (and min heap) include:
#getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
#extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(Log n)
#as this operation needs to maintain the heap property (by calling heapify()) after removing root.
#insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree.
#If new key is smaller than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
#Here we are going to implement a max-heap

import sys
class MaxHeap:

#The constructor initializes the heap with a maxsize entered by the user, size set to 0, all the elements of heap set to 0
#For the sake of easier calculation of parent and child nodes, we do the indexing from 1 instead of 0. So we fill the 0th index of heap with a garbage value
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1