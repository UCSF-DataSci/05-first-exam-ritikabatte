import sys

def complement(nucleotide):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                       'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join(complement_dict[base] for base in nucleotide)

def reverse(nucleotide):
    return nucleotide[::-1]

def reverse_complement(nucleotide):
    return reverse(complement(nucleotide))

def main():
    print("script started")
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <DNA_nucleotide>")
        sys.exit(1)

    nucleotide = sys.argv[1]

    # Perform operations
    original_strand = nucleotide
    complement_strand = complement(nucleotide)
    reverse_strand = reverse(nucleotide)
    reverse_complement_strand = reverse_complement(nucleotide)

    # Print results
    print(f"Original sequence: {original_strand}")
    print(f"Complement: {complement_strand}")
    print(f"Reverse: {reverse_strand}")
    print(f"Reverse complement: {reverse_complement_strand}")

if __name__ == "__main__":
    main()
    
