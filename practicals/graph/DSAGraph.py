from LinkedList import LinkedList
from DSANode import GrapNode
from DSACQueue import DSACQueue
from DSAStack import DSAStack


class Graph:
    def __init__(self):
        self.vertices = LinkedList()
        self.count = 0
    
    def getFristVetex(self):
        return self.vertices.head.key.label

    def addVertex(self, label, value):
        self.vertices.insert_sorted(GrapNode(label, value))
        self.count += 1

    def verticesCount(self):
        return self.count

    def getVertex(self, label):
        node = None
        for vertex in self.vertices:
            if vertex.label == label:
                node = vertex
        return node

    def checkVertexExist(self, label):
        check = False
        for vertex in self.vertices:
            if vertex.label == label:
                check = True
        return check

    def addEdge(self, label1, label2):
        self.getVertex(label1).addAdjac(self.getVertex(label2))
        self.getVertex(label2).addAdjac(self.getVertex(label1))
        
    def hasVertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                return True
        return False
    
    def getValue(self, label):
        val = None
        for vertex in self.vertices:
            if vertex.label == label:
                val = vertex.value
        return val

    def getAdjacent(self, label):
        AdjacentList = []
        for vertex in self.getVertex(label).adjacent:
            AdjacentList.append(vertex.label)
        return AdjacentList

    def display(self):
        for vertex in self.vertices:
            print(f"Vertex Label: {vertex.label}, ",end="")
            print(f"Value: {vertex.value}, ",end="")
            temp = self.getAdjacent(vertex.label)
            print(f"Adjacency: {temp}") if temp else print(f"Adjacency: None")
        print()

    def dfs(self, label):
        visited = []
        marked = []
        S = DSAStack(self.count)
        S.push(label)
        while not S.isEmpty():
            v = S.pop()
            if v not in marked:
                visited.append(v)
                marked.append(v)
                neighbor = self.getAdjacent(v)
                for w in neighbor:
                    if w not in marked:
                        S.push(w)
        return visited

    def bfs(self, label):
        visited = []
        marked = []
        Q = DSACQueue(self.count)
        Q.enqueue(label)
        while not Q.isEmpty():
            v = Q.dequeue()
            if v not in marked:
                visited.append(v)
                marked.append(v)
                neighbor = self.getAdjacent(v)
                for w in neighbor:
                    if w not in marked:
                        Q.enqueue(w)
        return visited

if __name__ == "__main__":
    G1 = Graph()
    G1.addVertex(1,"A")
    G1.addVertex(2,"B")
    G1.addVertex(3,"C")
    G1.addVertex(4,"D")
    G1.addVertex(5,"E")
    G1.addVertex(6,"F")
    G1.addEdge(1,3)
    G1.addEdge(2,3)
    G1.addEdge(3,4)
    print(G1.count)
    G1.display()
    print(G1.getFristVetex())
    print(G1.getValue(5))

