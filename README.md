# DNA Sequence Analyzer🧬

## Description

The "DNA Sequence Analyzer" project is a tool written in Python, allowing the analysis of DNA sequences from a FASTA file. The tool utilizes the BioPython library for efficient manipulation of genetic sequences and DNA analysis-related computations.

## Usage Instructions

1. Clone the repository or download the source files.
2. Install the necessary dependencies, including BioPython.

    ```bash
    pip install biopython
    ```

3. Run the `analyze_dna_sequence.py` script, providing the path to the FASTA file containing the DNA sequence of interest as an argument.

    ```bash
    python analyze_dna_sequence.py --file_path /path/to/file.fasta
    ```

## Functions

- **`analyze_dna_sequence(file_path)`**
  - Reads the DNA sequence from the FASTA file.
  - Computes the GC content in the sequence.
  - Finds and returns open reading frames (ORFs) of at least 50 amino acids in length.

## Results

- GC content in the sequence (in percentages).
- Number of found open reading frames (ORFs).
- Individual ORFs along with their ordinal numbers.

## Usage Example

```bash
python analyze_dna_sequence.py --file_path /path/to/file.fasta
