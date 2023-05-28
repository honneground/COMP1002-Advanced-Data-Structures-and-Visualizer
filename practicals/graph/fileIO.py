from DSAGraph import Graph


class FileIO:
    def __init__(self, filename):
        self.filename = filename

    def readGraph(self):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            # extract nodes and edges from file contents
        except:
            print("404 File not found.")
        try:
            nodes = []
            edges = []
            for line in lines:
                vertices = line.strip().split()
                if (vertices[1],vertices[0],) not in edges:
                    if vertices[0] not in nodes:
                        nodes.append(vertices[0])
                    if vertices[1] not in nodes:
                        nodes.append(vertices[1])
                    edges.append([vertices[0], vertices[1]])
            # create graph object
            graph = Graph()
            for node in nodes:
                if not graph.checkVertexExist(node):
                    graph.addVertex(node, None)
            for edge in edges:
                if edge[1] not in graph.getAdjacent(edge[0]):
                    graph.addEdge(edge[0], edge[1])
            return graph
        except:
            print("The file format incorrect.")


if __name__ == "__main__":
    graph = FileIO("graph_data").readGraph()
    print("Depth First Search",end="")
    print(graph.dfs("5"))
    print("Breadth First Search",end="")
    print(graph.bfs("8"))