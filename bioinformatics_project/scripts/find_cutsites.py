import sys

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequence = ''.join(line.strip() for line in file if not line.startswith('>'))
    return sequence

file_path = "/Users/ritikabatte02/bioinformatics_project/data/random_sequence.fasta"


def find_cut_sites(sequence, cut_site):
    cut_site_clean = cut_site.replace('|', '')
    locations = []
    start = 0
    while True:
        start = sequence.find(cut_site_clean, start)
        if start == -1:
            break
        locations.append(start)
        start += 1  
        
    return locations

def find_cut_site_pairs(locations, min_distance=80000, max_distance=120000):
    pairs = []
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = locations[j] - locations[i]
            if min_distance <= distance <= max_distance:
                pairs.append((locations[i], locations[j]))
    
    return pairs

def main():
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <FASTA_file> <cut_site_sequence>")
        sys.exit(1)
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]
    sequence = read_fasta(fasta_file)
    cut_site_locations = find_cut_sites(sequence, cut_site)
    cut_site_pairs = find_cut_site_pairs(cut_site_locations)
    print(f"Analyzing cut site: {cut_site}")
    print(f"Total cut sites found: {len(cut_site_locations)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(cut_site_pairs[:5]):
        print(f"{i + 1}. {pos1} - {pos2}")
    with open('/Users/ritikabatte02/bioinformatics_project/results/cutsite_summary.txt', 'w') as summary_file:
        summary_file.write(f"Analyzing cut site: {cut_site}\n")
        summary_file.write(f"Total cut sites found: {len(cut_site_locations)}\n")
        summary_file.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        summary_file.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(cut_site_pairs[:5]):
            summary_file.write(f"{i + 1}. {pos1} - {pos2}\n")

if __name__ == "__main__":
    main()

