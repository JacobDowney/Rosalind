"""
Complementing a Strand of DNA


Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

from io import StringIO

def complementing_a_strand_of_dna(filename):
    with open(filename, 'r') as file:
        reverse = file.read().strip()[::-1]
        complement = {'A' : 'T', 'T': 'A', 'G' : 'C', 'C' : 'G'}
        reverse_complement = StringIO()
        for base in reverse:
            reverse_complement.write(complement[base])
        return reverse_complement.getvalue()

def main():
    reverse_complement = complementing_a_strand_of_dna("rosalind_revc.txt")
    print(reverse_complement)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
