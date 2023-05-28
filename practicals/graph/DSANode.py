from LinkedList import LinkedList

class GrapNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.adjacent = LinkedList()

    def __iter__(self):
        return self.adjacent.__iter__()

    def __str__(self):
        return ("Label: " + str(self.label) + " Value: " + str(self.value) + "\n")

    def __lt__(self, other):
        return self.label < other.label


    def __gt__(self, other):
        return self.label > other.label


    def __eq__(self, other):
        return self.label == other.label


    def __le__(self, other):
        return self.label <= other.label


    def __ge__(self, other):
        return self.label >= other.label

    def __ne__(self, other):
        return self.label != other.label

    
    # def _adjSort(self):
    #     for i in range(1, len(self.adjacent)):
    #         key = self.adjacent[i]
    #         j = i - 1
    #         while j >= 0 and self.adjacent[j].label > key.label:
    #             self.adjacent[j + 1] = self.adjacent[j]
    #             j -= 1
    #         self.adjacent[j + 1] = key

    # I tried my best. but I failed.


    
    def addAdjac(self, toNode):
        self.adjacent.insert_sorted(toNode)
        # self._adjSort()
    