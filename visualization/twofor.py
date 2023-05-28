import graphviz
import os
from teardown import teardown

class Node:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def is_full(self):
        return len(self.keys) == 3

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.is_leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if self.children[i].is_full():
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        child = self.children[i]
        new_node = Node(is_leaf=child.is_leaf)

        self.keys.insert(i, child.keys[1])
        self.children.insert(i + 1, new_node)

        new_node.keys = child.keys[2:]
        child.keys = child.keys[:1]

        if not child.is_leaf:
            new_node.children = child.children[2:]
            child.children = child.children[:2]

    def draw(self, dot):
        node_label = ','.join(str(key) for key in self.keys if key is not None)
        node = str(id(self))

        dot.node(node, node_label)

        if self.is_leaf:
            return node

        for child in self.children:
            child_node = child.draw(dot)
            dot.edge(node, child_node)

        return node


class Tree:
    def __init__(self):
        self.root = Node(is_leaf=True)

    def insert(self, key):
        root = self.root
        if root.is_full():
            new_node = Node()
            self.root = new_node
            new_node.children.append(root)
            new_node.split_child(0)
            new_node.insert_non_full(key)
        else:
            root.insert_non_full(key)

    def draw(self, filename):
        dot = graphviz.Digraph(format='png')
        self.root.draw(dot)
        dot.render(filename, view=False)
        os.remove(filename)



def draw(arr, arrow_duplicate = True):
    teardown()
    tree = Tree()
    added = []
    for key in arr:
        if arrow_duplicate:
            added.append(key)
            tree.insert(key)
            tree.draw(f"234_step{len(added)}")
        else:
            if key not in added:            
                added.append(key)
                tree.insert(key)
                tree.draw(f"234_step{len(added)}")


def create_tree(arr, arrow_duplicate = True):
    tree = Tree()
    added = []
    for key in arr:
        if arrow_duplicate:
            added.append(key)
            tree.insert(key)
        else:
            if key not in added:            
                added.append(key)
                tree.insert(key)
    print(f"The nodes count in the 2-4 tree is {len(added)}")
    return tree

if __name__ == "__main__":
    array = [152, 83, -14, 9, 1, 9, 70, 42, 32, 32, 76, 19, 15, 78, 69, 54, 51, 41, 90, 9, 1, 33, 44, 13, 96, 24, 98]
    create_tree(array)

        
