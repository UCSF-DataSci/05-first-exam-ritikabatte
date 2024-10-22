mkdir -p bioinformatics_project
cd bioinformatics_project || exit
mkdir -p data scripts results
touch scripts/generate_fasta.py scripts/dna_operations.py scripts/find_cutsites.py
touch results/cutsite_summary.txt
touch data/random_sequence.fasta
echo "# Bioinformatics Project Details" > README.md
echo "This project has the following directories and files:" >> README.md
echo "- **data/**: has input data like FASTA files." >> README.md
echo "- **scripts/**: has python scripts for DNA operations and finding cut sites" >> README.md
echo "- **results/**: Has the summaries of cut sites." >> README.md
echo "Project Set up:"
tree ../bioinformatics_project


