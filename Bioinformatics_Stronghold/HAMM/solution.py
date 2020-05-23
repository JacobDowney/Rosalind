"""
Counting Point Mutations


Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched
symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""

def counting_point_mutations(filename):
    seqs = open(filename).read().strip().split()
    return len(list(filter(lambda b: b[0] != b[1], zip(seqs[0], seqs[1]))))

def main():
    hamming_distance = counting_point_mutations("rosalind_hamm.txt")
    print(hamming_distance)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
