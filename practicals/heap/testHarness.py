from DSAHeap import DSAHeap
from fileIO import *
import random

outfile = "outfile.csv"
infile = "RandomNames7000.csv"

priorityStep = 2 # feel free to editt
maxSize = 15
StartVal = 2


def quickEmpty(heap, time):
    for _ in range(time):
        delEntry = heap.remove()
        if delEntry != None:#The heap class would return None if there is nothoing to remove. else remove the heap enrty removed.
            print(f"Removed current root entry of ({delEntry}) from the heap.")
        else:
            print(f"Attempt failed! The heap is empty. Nothing to remove!")
        heap.displayPri(False)
        print()

def generateNumbers(start, increment, numElements):
    numbers = []
    currentNumber = start
    for _ in range(numElements):
        numbers.append(currentNumber)
        currentNumber += increment
    return numbers

def autoValFill(num):
    num = int(num/priorityStep)
    return _autoValFill(num)

def _autoValFill(num):
    letters = []
    while num > 0:
        num -= 1
        letters.append(chr(num % 26 + ord('A')))
        num //= 26
    return ''.join(reversed(letters))

def main():
    print("\n\n------------------ # Test Harness of Practical 7 #  ------------------\n")

    print("\n------------------1. Creating a heap------------------\n\n")

    print(f"# Empty heap at a size of number {maxSize} initialized.")
    heap = DSAHeap(maxSize)
    print(f"(As the worksheet requested the elements in the heap can not go over the max capacity of the heap.)")
    print("\n# Testing add value function.\n")
    print(f"(The testHarness would add {maxSize+1} heap entry to the haep in a stable random order by using a random seed,")
    print(" the extra one run is designed to test the the robustness of the heap class)\n")
    random.seed(42)
    inPutList = []
    for i in range(StartVal,priorityStep*maxSize+StartVal,priorityStep):
        inPutList.append(i)
    random.shuffle(inPutList) # shuffle the inPutList to a stable random order for sorting testing later
    inPutList.append(priorityStep*maxSize+StartVal)
    for pri in inPutList:
        val = autoValFill(pri)
        if heap.add(pri, val) == 0:# return 0 mean things goes well, return 1 means fail
            print(f"Successfully added the value \"{val}\" with a priority of \"{pri}\" to the heap. Now heap count is {heap.getCount()}.")
        else:
            print(f"Ops! Added value \"{val}\" with a priority of \"{pri}\" unsuccessfully. We reach the limit of the heap at {heap.getMax()}. There is already {heap.count} entries in the heap.")
    print("\n(Messages were printed after confirmation of the adding.)\n") 
    print("\n# Testing four types of display function.\n")
    print("1.",end="")
    heap.displayPriArr()
    print("\n2.",end="")
    heap.displayPri()
    print("\n3.",end="")
    heap.displayArr()
    print("\n4.",end="")
    heap.display()
    print("\nIn the following testing, the most appropriate display would be adopted for different scenarios.")
    print("\nThe \"remove\" function will be tested after performing the heap sort. Therefore, the root entry removed would correspond to the entry with the maximum priority, which logically aligns with the intended behaviour.")

    print("\n\n\n------------------2. Heap Sort------------------\n")

    print("\n# Testing sortting function.\n")
    print("Calling the heapSort() to sort the heap...\n")
    heap.heapSort()
    print("Heap sorted. Display the heap array and heap priorities array for confirmation.\n")
    heap.displayPriArr()
    heap.displayArr()
    print("\n# Testing remove root entry function.\n")
    print(f"Executing the remove function {maxSize+1} times, and the extra one run is designed to test the the robustness of the heap class.")
    print("(State indicating messages along with the heap priorities by level will be displayed after each removal.)\n")

    quickEmpty(heap, maxSize+1)


    print("Execution completed. Display the heap array array for confirmation.\n")
    heap.displayArr()
    print("\nWe were expecting to see that the array is empty.")

    print("\n\n\n------------------3. File IO------------------\n\n")
    print("# Test storing in a large dataset\n")
    print("Executing this may cause the previous content to not be displayed due to the limited length of the terminal display.")
    input("\nPress \"Enter\" to continue...")

    print("\nInserting entries from the random names csv file as input to a new hash table...\n")
    Readin = readPuts(infile)
    print("Successfully read the file to the heap.\n")
    print(f"The maximum size of read-in heap is {len(Readin.heap)}, and enties counts is {Readin.getCount()}.\n")
    print("Please note, unlike keys, as the definition of the heap, different values can use the same property, so overwrite will not occur when reading files. And as heap sort is a stable sorting method, shared property entries will be in the same order as they were entered.\n")
    print("Processing to sort the read-in data...\n")
    if Readin.heapSort() is not None:
        print("Successfully sorted the read data")
    else:
        print("Ops! Fail to sort the data.")
    print(f"\nPrinting entries from the sorted heap to the {outfile}...")
    writePuts(Readin, outfile)  
    input("\nPress \"Enter\" to display sorted the read-in heap priorities array ...")
    print()
    Readin.displayPriArr()
    print("\nNote: There are some duplicates in the file that would not overwrite previous entries in the heap, so some properties may appear in the priorities array multiple times.")
    print(f"\nDue to the limited length of the terminal display, you are unlikely to see the entire heap display.\nHowever, you can find the sorted heap, including student names and their IDs, in the output CSV file named '{outfile}' in the folder. Please check the file for more information.")
    print("\n------------------ End ------------------\n")
    

# print(autoValFill(2))
# print(autoValFill(4))
# print(autoValFill(6))

main()
