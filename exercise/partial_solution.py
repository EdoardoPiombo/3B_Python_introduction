#Import sequnce fro file
with open("exercise/sequence.fasta") as file:
    lines = file.readlines()
sequence = lines[-1]

#State genetic code
GenCode = {'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*', 'TGC': 'C', 'TGT': 'C', 'TGA': 'W', 'TGG': 'W', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'ATA': 'M', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': '*', 'AGG': '*', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G' }

#Extract correct subsequence
sequence = sequence[8:]

#Divide sequence in codons
codons = [sequence[x:x+3] for x in range(0, len(sequence), 3)]

#Extract protein sequence
protein_sequence = ""
for codon in codons:
  #Stop the loop if the codon is a stop codon
  if GenCode[codon] == "*" :
    ?
  #Add the new aminoacid to protein_sequence
  protein_sequence = ?
 
