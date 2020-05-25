from Bio import SeqIO

fastas = list(SeqIO.parse(open('example.fasta'), 'fasta'))
profile_matrix = []
for i in range(len(fastas[0].seq)):
    profile_matrix.append([0] * 4)
map = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
for fasta in fastas:
    for i in range(0, len(fasta.seq)):
        profile_matrix[i][map[fasta.seq[i]]] += 1

rev_map = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
rtn = ""
for list in profile_matrix:
    rtn += rev_map[list.index(max(list))]
print(rtn)

for key in map:
    str_ = key + ": "
    for i in range(len(profile_matrix)):
        str_ += str(profile_matrix[i][map[key]]) + " "
    print(str_)
