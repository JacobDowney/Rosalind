"""
Transcribing DNA into RNA


Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

def transcribing_dna_into_rna(filename):
    with open(filename, 'r') as file:
        return(file.read().strip().replace('T', 'U'))

def main():
    rna = transcribing_dna_into_rna("rosalind_rna.txt")
    print(rna)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
