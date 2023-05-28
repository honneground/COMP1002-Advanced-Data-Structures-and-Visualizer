# Data Structures Assignment and Verification Tools

- **Unit**: Data Structures and Algorithms (`COMP1002` / `DSA1002`) — Assignment 2
- **Study Period**: 2023 Trimester 1A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 89 (High Distinction)

## Assignment context

This assessment combined executable answers with written reasoning and step-by-step diagrams. Its topics included data-structure selection, sorting and recursion, expression term counting with a stack, a bounded print queue, tree construction, graph traversal, heap insertion/deletion and hash-table probing.

Some questions required manual diagrams or worked steps. I developed companion programs to verify those steps and generate figures, alongside the four submitted scripts.

## Repository contents

| Directory | Contents |
|---|---|
| `submission/` | The four submitted scripts and the author's hash-workings CSV |
| `visualization/` | Tree/heap drawing, graph-traversal traces, heap-deletion and hashing helpers used to inspect worked examples |
| `practicals/graph/` | Custom graph/linked-list/stack/queue implementation and its original practical harness |
| `practicals/heap/` | The coherent bounded-heap practical implementation, file I/O, sample records and harness |
| `assets/` | Selected insertion and deletion diagrams demonstrating the visual output |

### Submitted scripts

- `submission/2D.py`: converts an iterative factorial-based calculation into recursion with a wrapper, exception handling and printed example cases.
- `submission/3A.py`: uses a NumPy-backed stack to compare the number of terms on the two sides of an equality.
- `submission/3B.py`: implements a capacity-100 print queue on a double-ended singly linked list and demonstrates attempts to enqueue and dequeue 102 jobs.
- `submission/5D.py`: stores a binary tree in an array and displays levels using the child-index rules.
- `submission/hash.csv`: worked hash-table insertion/probing output supporting the written analysis.

### Verification and visualization tools

`visualization/bst.py` and `rbt.py` use **bintrees** for the underlying tree algorithms and **Graphviz** to export the evolving structures. The scripts automate diagram generation and inspection of tree changes.

`visualization/heap.py` wraps Python's **heapq** for step-by-step min-heap drawings. `heap_way_tree.py` instead draws the array values in binary-tree layout. `twofor.py` contains a separate 2-3-4 tree insertion/splitting implementation and drawing functions. `graph.py` prints DFS/BFS frontier and path states for its included example graph.

`visualization/heap_deletion/DSAHeap.py` is the author's custom heap variant with insertion, arbitrary-value deletion and intermediate Graphviz drawings. It negates priorities in the included example to demonstrate min-heap behavior using its maximum-priority implementation. `visualization/hashing/hashtable.py` prints hash calculations and appends insertion traces to CSV.

The practical heap implementation includes its own entry class, file I/O and harness in `practicals/heap/`.

## Selected output

![Final insertion state](assets/heap_step26.png)

![Heap deletion trace](assets/step_2_5.png)

## Run the submitted examples

Use Python 3 and NumPy. From this project directory:

```bash
python -m pip install numpy
python submission/2D.py
python submission/3A.py
python submission/3B.py
python submission/5D.py
```

The examples print their own result or demonstration sequence.

## Run the tools

Drawing tools additionally use the Python `graphviz` package and a Graphviz installation with `dot` available on PATH. The BST/RBT tools also import `bintrees`; the graph practical's plotting helper imports `networkx` and `matplotlib`.

```bash
python -m pip install graphviz bintrees networkx matplotlib
cd visualization
python heap.py
python bst.py
python rbt.py
python heap_way_tree.py
python graph.py
cd heap_deletion
python DSAHeap.py
```

The drawing scripts write output to the current working directory. The 2-3-4 tree's drawing helper clears PNG files there before producing a new sequence, so use a separate output directory when calling `twofor.draw(...)`; the selected repository illustrations are in `assets/`.

For the original practical demonstrations, run from each directory so relative input filenames resolve:

```bash
cd practicals/graph
python testHarness.py
```

```bash
cd practicals/heap
python testHarness.py
```

The heap harness pauses for Enter and writes `outfile.csv`. The graph harness uses the included `prac6_1.al` and `prac6_2.al` adjacency-list inputs.
