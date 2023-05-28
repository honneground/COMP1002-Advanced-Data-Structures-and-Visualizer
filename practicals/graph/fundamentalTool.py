import networkx as nx 
import matplotlib.pyplot as plt

def autoValFill(num):
    letters = []
    while num > 0:
        num -= 1
        letters.append(chr(num % 26 + ord('A')))
        num //= 26
    return ''.join(reversed(letters))


def plot_graph_from_file(file_path):
    # Create an empty graph
    graph = nx.Graph()

    # Read the file and add edges to the graph
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two nodes
            source, target = line.strip().split()

            # Add an undirected edge between the nodes
            graph.add_edge(source, target)

    # Draw the graph
    nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray')

    # Display the plot
    plt.show()

if __name__ == "__main__":
    plot_graph_from_file("prac6_1.al")
    plot_graph_from_file("prac6_2.al")