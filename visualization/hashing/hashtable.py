import csv
from teardown import teardown

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash1(self, key):
        checksum = 11169
        the_end = ", "
        sumlist = []
        for i in range(len(key)):
            if i+1 == len(key):
                the_end = "\n"
            ch = key[i]
            checksum = checksum + ord(ch) + 8
            sumlist.append(ord(ch))
            print(f"ASCII({ch}) = {ord(ch)}", end=the_end)
        sum_string = " + ".join(str(num) for num in sumlist)
        print(f"checksum = 11169 + sum(ASCII(ch) + 8)\n         = 11169 + 8 × {len(sumlist)} + {sum_string} \n         = {checksum}")  
        hashIdx = checksum % self.size
        print(f"HashIdx = checksum % tablesize\n        = {checksum} % {self.size}\n        = {hashIdx}")
        return hashIdx

    def rehash(self, oldhash):
        newhash = (oldhash + self.size // 2) % self.size
        return newhash

    def insert(self, key, value):
        print("#",value, key)
        hashIdx = self.hash1(key)
        if self.table[hashIdx] is None:
            self.table[hashIdx] = (key, value)
            print(f"As slot {hashIdx} is empty, we can fill th the slot with the student key-value pair.\n")
            self.count += 1
        else:
            # Linear probing to find the next available slot
            nextIdx = self.rehash(hashIdx)
            while self.table[nextIdx] is not None and nextIdx != hashIdx:
                nextIdx = self.rehash(nextIdx)
            if nextIdx == hashIdx:
                raise Exception("Hashtable is full.")
            self.table[nextIdx] = (key, value)
            self.count += 1

    def get(self, key):
        hashIdx = self.hash1(key)
        if self.table[hashIdx] is not None and self.table[hashIdx][0] == key:
            return self.table[hashIdx][1]
        else:
            # Linear probing to find the key
            nextIdx = self.rehash(hashIdx)
            while self.table[nextIdx] is not None and (self.table[nextIdx][0] != key or nextIdx != hashIdx):
                nextIdx = self.rehash(nextIdx)
            if nextIdx == hashIdx or self.table[nextIdx] is None:
                raise KeyError("Key not found in hashtable.")
            return self.table[nextIdx][1]
        
    def display(self):
        print("Index |   Key   | Value")
        print("------|---------|-----------")
        for i, item in enumerate(self.table):
            key = item[0] if item is not None else ""
            value = item[1] if item is not None else ""
            print(f"{i:5} | {key:7} | {value:5}")

    def append_to_csv(self, filename="outfile.csv"):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'step {self.count}'])
            writer.writerow(['Index', 'Key', 'Value'])
            for i, item in enumerate(self.table):
                key = item[0] if item is not None else ""
                value = item[1] if item is not None else ""
                writer.writerow([i, key, value])


# Create a hashtable with size 17
teardown()
ht = HashTable(17)
array = [("Sam","Student 1"),
("Josh","Student 2"),
("David","Student 3"),
("Young","Student 4"),
("Ali","Student 5"),
("Ozzie","Student 6"),
("Michael","Student 7")]
# Insert key-value pairs
for student in array:
    ht.insert(student[0], student[1])
    ht.append_to_csv()

