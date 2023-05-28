from DSAHeap import DSAHeap

def readPuts(filename):
    try:
        with open(filename, "r") as fileobj:
            try:
                contents = fileobj.readlines()
                table = DSAHeap(len(contents))
                for line in contents:
                    splitLine = line.strip().split(",")
                    table.add(int(splitLine[0]), splitLine[1])
            except:
                print("\nThe file format incorrect.")
                table = None
    except:
        print("\n404 File not found.")
        table = None
    return table

def writePuts(table, filename):
    try:
        with open(filename, "w") as fileobj:
            for entry in table.heap[:table.getCount()]:
                line = f"{entry.getPri()},{entry.getVal()}\n" 
                fileobj.write(line)
        print(f"\nHeap successfully written to {filename}")
    except:
        print("Error occurred while writing the heap to file.")