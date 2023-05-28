from collections import deque

def graph_search(graph, start_node, algorithm='DFS'):
    visited = set()
    path = []
    if algorithm == 'DFS':
        stack = [(start_node, [start_node])]
        storage = stack
    elif algorithm == 'BFS':
        queue = deque([(start_node, [start_node])])
        storage = queue
    else:
        raise ValueError("Invalid algorithm specified. Please choose 'DFS' or 'BFS'.")

    while storage:
        current_node, path = storage.pop() if algorithm == 'DFS' else storage.popleft()
        visited.add(current_node)
        
        print(f"Current Node: {current_node}")
        print(f"{algorithm} Path: {' -> '.join(path)}")
        
        if current_node in graph:
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    storage.append((neighbor, new_path))
                    visited.add(neighbor)
        
        print(f"{algorithm} {storage.__class__.__name__}: {list(storage)}")
        print()

# Example usage
# Define a graph as an adjacency list
example_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Depth-First Search
print("Depth-First Search:")
graph_search(example_graph, 'A', algorithm='DFS')

print("------------------------")

# Breadth-First Search
print("Breadth-First Search:")
graph_search(example_graph, 'A', algorithm='BFS')
