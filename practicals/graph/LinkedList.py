from LinkedListNode import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def __iter__(self):
        current = self.head
        while current:
            yield current.key
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.key
            current = current.prev

    def __next__(self):
        if self.current is None:
            raise StopIteration
        key = self.current.key
        self.current = self.current.next
        return key
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        current = self.head
        nodes = []
        nodes.append("Head")
        while current:
            nodes.append(str(current.key))
            current = current.next
        nodes.append("Tail")
        return ' <--> '.join(nodes)

    def isEmpty(self):
        return self.size == 0

    def display(self):
        print(self)

    def insertFirst(self, key):
        node = LinkedListNode(key)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertLast(self, key):
        node = LinkedListNode(key)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            return None
        else:
            return self.head.key

    def peekLast(self):
        if self.isEmpty():
            return None
        else:
            return self.tail.key

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            key = self.head.key
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return key

    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            key = self.tail.key
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return key

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_sorted(self, key):
        node = LinkedListNode(key)
        if self.isEmpty() or key < self.head.key:
            self.insertFirst(key)
        elif key >= self.tail.key:
            self.insertLast(key)
        else:
            current = self.head
            while current.next:
                if key >= current.key and key <= current.next.key:
                    next_node = current.next
                    current.next = node
                    node.prev = current
                    node.next = next_node
                    next_node.prev = node
                    self.size += 1
                    return
                current = current.next

if __name__ == "__main__":
    L = LinkedList()
    L.insert_sorted(1)
    L.insert_sorted(2)
    L.insert_sorted(3)
    print(L.peekFirst())
    print(L.peekLast())
    print(L.removeFirst())
    print(L.removeLast())
    print(L.peekFirst())
    print(L.peekLast())
    print(L.isEmpty())
    L.clear()
    print(L.isEmpty())
    for i in range(20,0,-1):
        L.insert_sorted(i)
    L.display()
    print(str(L))
    print(L.size)