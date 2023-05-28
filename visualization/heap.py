import heapq
from graphviz import Digraph
import os

class Heap():
    def __init__(self):
        self.heap = []

    def insert(self, key):
        heapq.heappush(self.heap, key)

    def draw(self, filename):
        dot = Digraph()
        self._draw_recursive(dot, 0)
        dot.render(filename, format='png', view=False)
        os.remove(filename)

    def _draw_recursive(self, dot, index):
        if index < len(self.heap):
            dot.node(str(index), str(self.heap[index]))
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index < len(self.heap):
                dot.edge(str(index), str(left_child_index))
                self._draw_recursive(dot, left_child_index)
            if right_child_index < len(self.heap):
                dot.edge(str(index), str(right_child_index))
                self._draw_recursive(dot, right_child_index)

if __name__ == "__main__":
    heap = Heap()
    array = [152, 83, -14, 9, 1, 9, 70, 42, 32, 32, 76, 19, 15, 78, 69, 54, 51, 41, 90, 9, 1, 33, 44, 13, 96, 24, 98]
    for i, key in enumerate(array):
        heap.insert(key)
        print(heap.heap)

        heap.draw(f"heap_step{i}")
    