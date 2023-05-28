import numpy as np
from DSAHeapEntry import DSAHeapEntry
from graphviz import Digraph
import os

class DSAHeap:
    def __init__(self, maxSize):
        self.heap = np.empty(maxSize, dtype=object)
        self.count = 0

    def getCount(self):
        return self.count
    
    def getMax(self):
        return len(self.heap)

    def add(self, priority, value):
        if self.count == len(self.heap):
            state = 1
        else:
            entry = DSAHeapEntry(priority, value)
            self.heap[self.count] = entry
            self.trickleUp(self.count)
            self.count += 1
            state = 0
        return state
    
    def remove_val(self, inValue):
        index = None
        for i in range(self.count):
            if self.heap[i].value == inValue:
                index = i
                break
        if index is None:
            return None

        return self.remove_index(index)
    
    def remove_index(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        while index > 0:
            parent_index = (index - 1) // 2
            self.swap(index, parent_index)
            self.quick_draw()
            index = parent_index
        return self.remove()

    def remove(self):
        if self.count == 0:
            root = None
        else:
            root = self.heap[0]
            self.count -= 1
            self.heap[0] = self.heap[self.count]
            self.quick_draw()
            self.trickleDown(0)
            self.heap[self.count] = None
        return root

    def heapSort(self):
        temp = self.count
        sortedHeap = np.empty(self.count, dtype=object)
        index = 0
        while self.count > 0:
            sortedHeap[index] = self.remove()
            index += 1
        newArray = np.empty(len(self.heap), dtype=object)
        newArray[:temp] = sortedHeap
        self.heap = newArray
        self.count = temp
        return sortedHeap

    def heapify(self, arr):
        self.count = len(arr)
        self.heap[:self.count] = arr
        for i in range(self.count // 2 - 1, -1, -1):
            self.trickleDown(i)

    def trickleUp(self, index):
        if index == 0:
            return
        parentIndex = (index - 1) // 2
        if self.heap[index].getPri() > self.heap[parentIndex].getPri():
            self.swap(index, parentIndex)

            self.trickleUp(parentIndex)

    def trickleDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        largest = index

        if leftChildIndex < self.count and self.heap[leftChildIndex].getPri() > self.heap[largest].getPri():
            largest = leftChildIndex

        if rightChildIndex < self.count and self.heap[rightChildIndex].getPri() > self.heap[largest].getPri():
            largest = rightChildIndex

        if largest != index:
            self.swap(index, largest)
            self.quick_draw()
            self.trickleDown(largest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def display(self):
        print("Heap by Level:")
        level = 0
        levelStartIndex = 0
        NodesInLevel = 1
        while levelStartIndex < self.count:
            levelEndIndex = min(levelStartIndex + NodesInLevel, self.count)
            entries = self.heap[levelStartIndex:levelEndIndex]
            print(f"Level {level}:", end=" ")
            for entry in entries:
                if entry is not None:
                    print(f"'{entry}'", end=" ")
                else:
                    print("None", end=" ")
            print()
            levelStartIndex = levelEndIndex
            NodesInLevel *= 2
            level += 1

    def displayPri(self, title = True):
        if title == True:
            print("Heap Priorities by Level:")
        level = 0
        levelStartIndex = 0
        NodesInLevel = 1
        while levelStartIndex < self.count:
            levelEndIndex = min(levelStartIndex + NodesInLevel, self.count)
            entries = self.heap[levelStartIndex:levelEndIndex]
            print(f"Level {level}:", end=" ")
            for entry in entries:
                if entry is not None:
                    print(entry.getPri(), end=" ")
                else:
                    print("None", end=" ")
            print()
            levelStartIndex = levelEndIndex
            NodesInLevel *= 2
            level += 1

        
    def displayPriArr(self):
        priorities = [-(entry.getPri()) for entry in self.heap[:self.count]]
        print(priorities)

    def displayArr(self):
        entry = [str(entry) for entry in self.heap[:self.count]]
        print("Heap Array:", entry)

    def draw(self, filename):
        dot = Digraph()
        self._draw_recursive(dot, 0)
        dot.render(filename, format='png', view=False)
        os.remove(filename)

    def _draw_recursive(self, dot, index):
        if index < self.count:
            dot.node(str(index), str(self.heap[index]))
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index < self.count:
                dot.edge(str(index), str(left_child_index))
                self._draw_recursive(dot, left_child_index)
            if right_child_index < self.count:
                dot.edge(str(index), str(right_child_index))
                self._draw_recursive(dot, right_child_index)
    
    def quick_draw(self):
        global counter
        global delno
        self.draw(f"step_{delno}_{counter}")
        print(f"# {counter}")
        self.displayPriArr()
        counter += 1


if __name__ == "__main__":
    
    heap = DSAHeap(100)
    array = [152, 83, -14, 9, 1, 9, 70, 42, 32, 32, 76, 19, 15, 78, 69, 54, 51, 41, 90, 9, 1, 33, 44, 13, 96, 24, 98]
    for i, key in enumerate(array):
        heap.add(-key, key)

    heap.draw("step_0_0")

    for i, key in enumerate([78 ,13]):
        counter = 0
        delno = i+1
        heap.remove_val(key)