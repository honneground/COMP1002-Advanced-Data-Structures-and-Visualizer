import numpy as np
from DSAHeapEntry import DSAHeapEntry

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

    def remove(self):
        if self.count == 0:
            root = None
        else:
            root = self.heap[0]
            self.count -= 1
            self.heap[0] = self.heap[self.count]
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
        priorities = [entry.getPri() for entry in self.heap[:self.count]]
        print("Heap Priorities Array:", priorities)

    def displayArr(self):
        entry = [str(entry) for entry in self.heap[:self.count]]
        print("Heap Array:", entry)