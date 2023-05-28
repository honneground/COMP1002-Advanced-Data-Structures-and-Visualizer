import numpy as np

class DSAQueue:

    def __init__(self, capacity):

        self._capacity = capacity
        self._arr = np.empty(self._capacity, dtype=object)
        self._front = 0
        self._rear = -1
        self._count = 0
    
    def isEmpty(self):

        return self._count == 0
    
    def isFull(self):

        return self._count == self._capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self._rear += 1
            self._arr[self._rear] = item
            self._count += 1
        else:
            raise Exception("Queue is full")
    
    def dequeue(self):
        if not self.isEmpty():
            item = self._arr[self._front]
            self._front += 1
            self._count -= 1
            return item
        else:
            raise Exception("Queue is empty!!!")
    
    def getCount(self):
        return self._count
    
    def peek(self):
        if self.isEmpty():
            return None
        return self._arr[self._front]
    
if __name__ == "__main__":
        qqq = DSAQueue(3)
        qqq.enqueue("A")
        qqq.enqueue("B")
        qqq.enqueue("C")
        qqq.dequeue()
        qqq.enqueue("D")

