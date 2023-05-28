from DSAGraph import Graph
from fileIO import FileIO
import fundamentalTool

verticesNumber = 10
# better to use an even to test out more features, eg.10

def quickInsert(graph, nodes):
    for node in nodes:
        graph.addVertex(node, fundamentalTool.autoValFill(node)) #start from 1


def quickEdgeCreater(graph, numberOfNodes):
    limite = int(numberOfNodes/2)
    for i in range(1,limite+1):
        graph.addEdge(i, 2*i)
        print(f"Link vertext labeled {i} to vertext labeled {2*i}.")
        if 2*i != numberOfNodes:
            graph.addEdge(i, 2*i+1)
            print(f"Link vertext labeled {i} to vertext labeled {2*i+1}.")

def quickFindTest(graph, labels):
    for label in labels:
        node_vaule = graph.getValue(label)
        print(f"Node to find: {label}, Node Value: {node_vaule}, Reference Value: {fundamentalTool.autoValFill(label)}")

def main():
    print("\n\n\n------------------ Test Harness of Practical 6  ------------------\n\n")
    print("\n\n\n------------------0. UML Diagrams------------------\n\n")
    print("# Please see the ziped folder pdf file named \"uml_diagram_p6.pdf\"")
    print("\n\n\n------------------2. Graph Implementation------------------\n\n")
    graph0 = Graph()
    print("# Empty Graph initialized.")
    print("\n# Testing add vertex function.\n")
    print(f"Adding vertex of label from 1 to {verticesNumber} to the Graph.\n")
    quickInsert(graph0, list(range(1, verticesNumber+1, 1)))
    print("\n# Testing add edge function.\n")
    print(f"Adding some edge in between vertices.\n")
    quickEdgeCreater(graph0, verticesNumber)
    print("\n# Testing get value function.\n")
    print(f"Find the value of vertex with label from 1 to {verticesNumber} from the Graph.\n")
    quickFindTest(graph0,range(1,verticesNumber+1,1))
    print("\nWe expect the finded value to match the referring value.")
    print("\n# Testing display function.\n")
    print("(Also get getAdjacent function which called by display function.)\n")
    graph0.display()
    print("\n\n\n------------------2. Read Graph From File------------------\n\n")
    print("Reading two all file and convert into graph1 and graph2 using FileIO Class.\n")
    graph1 = FileIO("prac6_1.al").readGraph()
    graph2 = FileIO("prac6_2.al").readGraph()
    print("Displaying graph1 and graph2 to check the FileIO.\n")
    print("graph1 FROM prac6_1.al\n")
    graph1.display()
    print("graph2 FROM prac6_2.al\n")
    graph2.display()
    print("\n\n\n------------------3. Implement Depth First Search / Breadth First Search------------------\n\n")

    print("Test depth First Search and breadth First Search methods against the graphs from Activity 2.\n")
    print("graph1 FROM prac6_1.al\n")
    print("Depth First Search:   ",end="")
    print(graph1.dfs(graph1.getFristVetex()))
    print("Breadth First Search: ",end="")
    print(graph1.bfs(graph1.getFristVetex()))
    print("\ngraph2 FROM prac6_2.al\n")
    print("Depth First Search:   ",end="")
    print(graph2.dfs(graph2.getFristVetex()))
    print("Breadth First Search: ",end="")
    print(graph2.bfs(graph2.getFristVetex()))
    print("\nNote that all searches are started from the vertex added first to the graph.\n")
    print("\n------------------------------------\n")
    print("Note: The variable \"verticesNumber\" can be modified to control the number of vertices in the graph of part 1.")
    print("\n\n\n------------------ End ------------------\n\n")

main()
