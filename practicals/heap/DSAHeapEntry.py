class DSAHeapEntry:
    def __init__(self, inPri, inVal):
        self.priority = inPri
        self.value = inVal

    def getPri(self):
        return self.priority

    def setPri(self, priority):
        self.priority = priority

    def getVal(self):
        return self.value

    def setVal(self, value):
        self.value = value

    def __str__(self):
        return f"Priority: {self.priority}, Value: {self.value}"