class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.count = 0

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0
    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            new_node.count += 1
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data == current_node.data:
                    current_node.count += 1
                elif data < current_node.data:
                    # left
                    if not current_node.left:
                        new_node.count += 1
                        current_node.left = new_node
                        return
                    current_node = current_node.left
                else:
                    # right
                    if not current_node.right:
                        new_node.count += 1
                        current_node.right = new_node
                        return
                    current_node = current_node.right
        self.no_of_nodes += 1

    def lookUp(self, data):
        if self.root == None:
            return "Tree is empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    def remove(self, data):
        if self.root == None:
            return "Empty"
        current_node = self.root
        parent_node = None
        while current_node:
            if data < current_node.data:
                # left
                parent_node = current_node
                current_node = current_node.left
            elif data > current_node.data:
                # right
                parent_node = current_node
                current_node = current_node.right
            elif data == current_node.data:
                # we have match get to work!
                # Case 1: no child
                if current_node.right == None and current_node.left == None:
                    if current_node.data > parent_node.data:
                        parent_node.right = None
                    else:
                        parent_node.left = None
                # Case 2: 2 childs
                elif current_node.right and current_node.left:
                        temp_node = current_node.right
                        temp_parent_node = current_node
                        while temp_node.left:
                            temp_parent_node = temp_node
                            temp_node = temp_node.left
                          
                        if temp_node.data > temp_parent_node.data:
                            current_node.data = temp_node.data
                            if temp_node.right:
                                temp_parent_node.right = temp_node.right
                            else:
                                temp_parent_node.right = None
                        else:
                            current_node.data = temp_node.data
                            if temp_node.right:
                                temp_parent_node.left = temp_node.right
                            else:
                                temp_parent_node.left = None

                # case 3: 1 child
                else:
                    if current_node.left:
                        if current_node.data > parent_node.data:
                            parent_node.right = current_node.left
                        else:
                            parent_node.left = current_node.left
                    else:
                        if current_node.data > parent_node.data:
                            parent_node.right = current_node.right
                        else:
                            parent_node.left = current_node.right
                return True
        self.no_of_nodes -= 1

    def print_BST(self):
        print(self.root.data)
        left1 = self.root.left
        right1 = self.root.right
        print(f"{left1.data} {right1.data}")
        left1kaleft = left1.left
        left1karight = left1.right
        right1kaleft = right1.left
        right1karight = right1.right
        print(f"{left1kaleft.data} {left1karight.data} {right1kaleft.data} {right1karight.data}")
        right2 = right1karight.right
        left2 = right1karight.left
        print(left2.data, right2.data)   
    # Breadth First Search
    def breadthFirstSearch(self):
        currentNode = self.root
        list = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            list.append(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return list
    # Breadth First Search Recursive
    def breadthFirstSearchR(self, queue, list):
        if len(queue) == 0:
            return list
        currentNode = queue.pop(0)
        list.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.breadthFirstSearchR(queue, list)
    
    # Depth First Search
    def DFSInOrder(self):
        return traverseInOrder(self.root, [])
    
    def DFSPreOrder(self):
        return traversePreOrder(self.root, [])
    
    def DFSPostOrder(self):
        return traversePostOrder(self.root, [])

def traverseInOrder(node, list):
    if node.left:
        traverseInOrder(node.left, list)
    list.append(node.data)
    if node.right:
        traverseInOrder(node.right, list)
    return list

def traversePreOrder(node, list):
    list.append(node.data)
    if node.left:
        traversePreOrder(node.left, list)
    if node.right:
        traversePreOrder(node.right, list)
    return list

def traversePostOrder(node, list):
    if node.left:
        traversePostOrder(node.left, list)
    if node.right:
        traversePostOrder(node.right, list)
    list.append(node.data)
    return list


        
        







myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(20)
myBST.insert(1)
myBST.insert(6)
myBST.insert(15)
myBST.insert(170)

# print(myBST.breadthFirstSearch())
# print(myBST.breadthFirstSearchR([myBST.root], []))
print(myBST.DFSPostOrder())