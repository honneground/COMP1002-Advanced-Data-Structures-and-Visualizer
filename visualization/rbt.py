import bintrees
import graphviz
import os

def generate_tree(array):
    tree = bintrees.RBTree()
    added = []
    for value in array:
        if value not in added:
            added.append(value)
            tree.insert(value, value)
            export_tree_image(tree, f"rbt_step_{len(added)}")

def export_tree_image(tree, filename):
    dot = graphviz.Digraph()

    def add_nodes(node):
        if node is None:
            return
        color = 'red' if node.red else 'black'  # Set node color based on red or black
        dot.node(str(node.key), label=str(node.key), style='filled', fillcolor=color, fontcolor='white')
        if node.left is not None:
            dot.edge(str(node.key), str(node.left.key), label="L")
            add_nodes(node.left)
        if node.right is not None:
            dot.edge(str(node.key), str(node.right.key), label="R")
            add_nodes(node.right)

    add_nodes(tree._root)
    
    dot.format = 'png'
    dot.render(filename, view=False)
    os.remove(filename)

if __name__ == "__main__":
    array = sorted([152, 83, -14, 9, 1, 9, 70, 42, 32, 32, 76, 19, 15, 78, 69, 54, 51, 41, 90, 9, 1, 33, 44, 13, 96, 24, 98], reverse=True)
    generate_tree(array)
    print(len(array))