from DSAQueue import DSAQueue

class DSACQueue(DSAQueue):
    def __init__(self, capacity):
        super().__init__(capacity)
        self._front = -1
        self._rear = -1
    def enqueue(self, item):
        if self._rear - self._front == self._capacity - 1 or self._front - self._rear == 1:
            raise Exception("CQueue is full")
        elif (self._front == -1):
            self._front = 0
            self._rear = 0
            self._arr[self._rear] = item
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._arr[self._rear] = item
            # print("The item added is", item)
        self._count += 1
    def dequeue(self):
        if self._front == -1:
            raise Exception("CQueue is empty!!!")
        else:
            if self._front == self._rear:
                delete = self._arr[self._front]
                self._front = -1
                self._rear = -1
                # print("The item is removed is removed is: ",delete)
            else:
                delete = self._arr[self._front]
                self._front = (self._front + 1) % self._capacity
                # print("The item is removed is removed is", delete)
        self._count -= 1
        return delete