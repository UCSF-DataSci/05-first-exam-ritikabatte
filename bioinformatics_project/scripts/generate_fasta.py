import random 
import textwrap 


seq_length = 1000000
bases = ['A', 'C', 'G', 'T']
random_seq = ''.join(random.choices(bases, k=seq_length))
formatted_seq = '/n'.join(textwrap.wrap(random_seq, 80))
output_file = "/Users/ritikabatte02/bioinformatics_project/data/random_sequence.fasta"

with open(output_file, 'w') as fasta_file:
    fasta_file.write(">Random Sequence\n")
    fasta_file.write(formatted_seq)

print(f"Random DNA sequence generated and saved in {output_file}")
