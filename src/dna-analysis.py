from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def analyze_dna_sequence(file_path):
    with open(file_path, "r") as file:
        dna_sequence = SeqIO.read(file, "fasta").seq 
        gc_content = gc_fraction(dna_sequence)
        
       
        orfs = [orf for orf in dna_sequence.translate(table=1).split("*") if len(orf) > 50]
        return gc_content, orfs

file_path = "data/RecA-E.Coli.fasta" 
gc_content, orfs = analyze_dna_sequence(file_path)

print(f"GC Content: {gc_content:.2%}")
print(f"Number of Open Reading Frames: {len(orfs)}")


for i, orf in enumerate(orfs, start=1):
    print(f"ORF {i}: {orf}")
