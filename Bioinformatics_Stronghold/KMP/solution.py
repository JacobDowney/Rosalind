"""
Introduction to Random String


Problem
A prefix of a length n string s is a substring s[1:j]; a suffix of s is a
substring s[k:n].

The failure array of s is an array P of length n for which P[k] is the length
of the longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where
j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.

Sample Dataset
>Rosalind_87
CAGCATGGTATCACAGCAGAG
Sample Output
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

"""
C A G C A T G G T A T C A C A G C A G A G
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

import argparse
from Bio import SeqIO

def introduction_to_random_strings(filename):
    sequence = list(SeqIO.parse(open(filename), 'fasta'))[0].seq
    return get_failure_array(sequence)

# Made a seperate method because I'm gonna use it it my project
# Time Complexity: O(n)
# Space Complexity: O(n)
def get_failure_array(sequence):
    failure_array = [0] #* len(sequence)
    left = 0
    right = 1
    while right < len(sequence):
        while left != 0 and sequence[left] != sequence[right]:
            left = failure_array[left-1]
        if sequence[left] == sequence[right]:
            left += 1
        failure_array.append(left)
        right += 1
    return failure_array


def main():
    parser = argparse.ArgumentParser(description="solve with file")
    parser.add_argument('file_path', help='path to file', type=str)
    args = parser.parse_args()
    failure_array = introduction_to_random_strings(args.file_path)
    print(*failure_array)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
