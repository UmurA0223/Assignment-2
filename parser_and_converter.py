import Bio
from Bio import SeqIO
from Bio.Seq import IUPAC

file_path_1 = "/home/aslanm/Assignment-2/XM_024719586.1.fasta"
file_path_2 = "/home/aslanm/Assignment-2/NM_001103547.4.fasta"
file_path_3 = "/home/aslanm/Assignment-2/LR027377.1.fasta"
seq_handle_1 = SeqIO.parse(file_path_1, "fasta")
seq_handle_2 = SeqIO.parse(file_path_2, "fasta")
seq_handle_3 = SeqIO.parse(file_path_3, "fasta")

for seq_record in seq_handle_1:
	print(seq_record.id)
	print(seq_record.seq)

for seq_record in seq_handle_2:
        print(seq_record.id)
        print(seq_record.seq)

for seq_record in seq_handle_3:
        print(seq_record.id)
        print(seq_record.seq)

count_1 = SeqIO.convert(file_path_1, "fasta", "XM_024719586.genbank", "genbank", alphabet=IUPAC.ambiguous_dna)
count_2 = SeqIO.convert(file_path_2, "fasta", "NM_001103547.genbank", "genbank", alphabet=IUPAC.ambiguous_dna)
count_3 = SeqIO.convert(file_path_3, "fasta", "LR027377.genbank", "genbank", alphabet=IUPAC.ambiguous_dna)

print("Converted %i records" % count_1)
print("Converted %i records" % count_2)
print("Converted %i records" % count_3)

