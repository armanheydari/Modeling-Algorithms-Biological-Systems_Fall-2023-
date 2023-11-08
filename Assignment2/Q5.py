from Bio import SeqIO
from itertools import product
from suffix_trees import STree
import time

# Iterate through the sequences in the FASTA file and create the string file
t = time.time()
chromosome = ''
for record in SeqIO.parse('sequence.fasta', 'fasta'):
    chromosome += f">{record.id}\n{record.seq}\n"
    if len(chromosome) > 10000000:
        break
print('create string from fasta file time:', time.time() - t, 'seconds.')

# Generate suffix tree for the first 10000000 characters of the chromosome
t = time.time()
suffix_tree = STree.STree(chromosome[:10000000])
print('create suffix tree time:', time.time() - t, 'seconds.')

# Generate all possible 9mers
t = time.time()
all_9mers = [''.join(seq) for seq in product(['A', 'T', 'G', 'C'], repeat=9)]
print('generate all 9mers time:', time.time() - t, 'seconds.')

# Search for each 9mer in the suffix tree and store the count of matches
t = time.time()
results = {}
for mer in all_9mers:
    temp = len(suffix_tree.find_all(mer))
    if temp > 1000:
        results[mer] = temp
print('searching all 9mers in the suffix tree time:', time.time() - t, 'seconds.')

# Sort the results dictionary in descending order
t = time.time()
results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
print('sorting results time:', time.time() - t, 'seconds.')

# Output the results
print('Most frequent 9mers in the chromosome are:')
for key, value in results.items():
    print(key, ':', value)
