"""
Translating RNA into Protein


Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from
the English alphabet (all letters except for B, J, O, U, X, and Z). Protein
strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10
kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""

import argparse
from io import StringIO

codon_map = {
    'GCU' : 'A',    'GCC' : 'A',    'GCA' : 'A',    'GCG' : 'A',
    'UGU' : 'C',    'UGC' : 'C',
    'GAU' : 'D',    'GAC' : 'D',
    'GAA' : 'E',    'GAG' : 'E',
    'UUU' : 'F',    'UUC' : 'F',
    'GGU' : 'G',    'GGC' : 'G',    'GGA' : 'G',    'GGG' : 'G',
    'CAU' : 'H',    'CAC' : 'H',
    'AUU' : 'I',    'AUC' : 'I',    'AUA' : 'I',
    'AAA' : 'K',    'AAG' : 'K',
    'UUA' : 'L',    'UUG' : 'L',    'CUU' : 'L',    'CUC' : 'L',    'CUA' : 'L',    'CUG' : 'L',
    'AUG' : 'M',
    'AAU' : 'N',    'AAC' : 'N',
    'CCU' : 'P',    'CCC' : 'P',    'CCA' : 'P',    'CCG' : 'P',
    'CAA' : 'Q',    'CAG' : 'Q',
    'CGU' : 'R',    'CGC' : 'R',    'CGA' : 'R',    'CGG' : 'R',    'AGA' : 'R',    'AGG' : 'R',
    'UCU' : 'S',    'UCC' : 'S',    'UCA' : 'S',    'UCG' : 'S',    'AGU' : 'S',    'AGC' : 'S',
    'ACU' : 'T',    'ACC' : 'T',    'ACA' : 'T',    'ACG' : 'T',
    'GUU' : 'V',    'GUC' : 'V',    'GUA' : 'V',    'GUG' : 'V',
    'UGG' : 'W',
    'UAU' : 'Y',    'UAC' : 'Y',
    'UAA' : 'Stop', 'UAG' : 'Stop', 'UGA' : 'Stop',
}

def translating_rna_info_protein(filename):
    sequence = open(filename, 'r').read().strip()
    triplets = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    translation = StringIO()
    for triplet in triplets:
        amino_acid = codon_map[triplet]
        if amino_acid == 'Stop':
            return translation.getvalue()
        translation.write(amino_acid)
    return translation.getvalue()

def main():
    parser = argparse.ArgumentParser(description="solve with file")
    parser.add_argument('file_path', help='path to file', type=str)
    args = parser.parse_args()

    translation = translating_rna_info_protein(args.file_path)
    print(translation)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
