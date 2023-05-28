# Hash Insertion Trace

This author-developed helper calculates the hash and probe sequence for the assignment's worked insertion example. It writes each successive table state to `outfile.csv` and prints the arithmetic to the terminal.

The original cleanup helper expects an existing `outfile.csv` and clears PNG files in the working directory. Run the example in a separate output directory. From this directory:

```bash
mkdir -p output
cd output
python -c "open('outfile.csv', 'w').close()"
python ../hashtable.py
```

The resulting CSV records the insertion trace. The assignment's worked example is in `submission/hash.csv` at the project root.
