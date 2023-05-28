import numpy as np
from graphviz import Digraph

class ArrayBinaryTree:
    def __init__(self):
        self.tree = np.array([])

    def insert(self, value):
        if self.tree.size == 0:
            self.tree = np.array([value])
        else:
            self.tree = np.append(self.tree, value)

    def get_root(self):
        return self.tree[0] if self.tree.size > 0 else None

    def get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index < self.tree.size:
            return self.tree[left_child_index]
        return None

    def get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index < self.tree.size:
            return self.tree[right_child_index]
        return None
    
    def display(self):
        level = 0
        nodes_to_print = 1
        index = 0
        while index < self.tree.size:
            nodes = self.tree[index:index + nodes_to_print]
            print(", ".join([str(node) for node in nodes]))
            level += 1
            index += nodes_to_print
            nodes_to_print *= 2

    def draw(self):
        dot = Digraph()
        self._draw_recursive(dot, 0)
        dot.render('binary_tree', format='png', view=False)

    def _draw_recursive(self, dot, index):
        if index < self.tree.size:
            dot.node(str(index), str(self.tree[index]))
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index < self.tree.size:
                dot.edge(str(index), str(left_child_index))
                self._draw_recursive(dot, left_child_index)
            if right_child_index < self.tree.size:
                dot.edge(str(index), str(right_child_index))
                self._draw_recursive(dot, right_child_index)


tree = ArrayBinaryTree()

array = [152, 83, -14, 9, 1, 9, 70, 42, 32, 32, 76, 19, 15, 78, 69, 54, 51, 41, 90, 9, 1, 33, 44, 13, 96, 24, 98]

for key in array:
    tree.insert(key)

tree.display()
tree.draw()

