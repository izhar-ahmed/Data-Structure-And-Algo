# Implement graph using adjacency list (hash table)
class Graph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        if self.isExit(node):
            return "node is already exit"
        else:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    def addEdges(self, node1, node2):
        if not node1 or not node2:
            return "there is no such nodes"
        elif self.isConn(node1, node2):
            return "already have a connection"
        else:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)

    def isExit(self, node):
        for key in self.adjacentList:
            if key == node:
                return True
        return False
    
    def isConn(self, node1, node2):
        for node in self.adjacentList[node1]:
            if node == node2:
                return True
        return False

    def showAdjacentList(self):
        print(self.adjacentList)

    
myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdges('3', '1')
myGraph.addEdges('3', '4')
myGraph.addEdges('4', '5')
myGraph.addEdges('4', '2')
myGraph.addEdges('1', '2')
myGraph.addEdges('1', '0')
myGraph.addEdges('0', '2')
myGraph.addEdges('6', '5')







myGraph.showAdjacentList()