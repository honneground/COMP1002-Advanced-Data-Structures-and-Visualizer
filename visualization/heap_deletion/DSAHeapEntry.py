class DSAHeapEntry:
    def __init__(self, inPri, inVal):
        self.priority = inPri
        self.value = inVal

    def __str__(self):
        return str(self.value)

    def getPri(self):
        return self.priority

    def setPri(self, priority):
        self.priority = priority

    def getVal(self):
        return self.value

    def setVal(self, value):
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority


    def __gt__(self, other):
        return self.priority > other.priority


    def __eq__(self, other):
        return self.priority == other.priority


    def __le__(self, other):
        return self.priority <= other.priority


    def __ge__(self, other):
        return self.priority >= other.priority

    def __ne__(self, other):
        return self.priority != other.priority


    # def __str__(self):
    #     return f"Priority: {self.priority}, Value: {self.value}"