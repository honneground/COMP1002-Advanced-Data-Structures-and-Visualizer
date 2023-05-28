class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("Linked list is empty.")

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

        return data


class Queue(LinkedList):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue is full. Cannot add more printing jobs.")
        self.append(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty. No printing jobs available.")
        return self.remove_first()



queue = Queue(100)

# try to insert 102 random printing jobs
for i in range(102):
    try:
        queue.enqueue(f"Printing Job {i+1}")
        print(f"Enqueued: Printing Job {i+1}")
    except Exception as e:
        print(e)

print()

# try to dequeue 102 printing jobs from the queue
for i in range(102):
    try:
        job = queue.dequeue()
        print(f"Dequeued: {job}")
    except Exception as e:
        print(e)