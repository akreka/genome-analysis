
def validate_sequence(sequence: str) -> bool:
    """
    Check whether a DNA sequence contains only valid nucleotides.

    Valid nucleotides: A, T, G, C.
    """

    valid_nucleotides = {"A", "T", "G", "C"}

    sequence = sequence.upper()

    return bool(sequence) and all(
        nucleotide in valid_nucleotides
        for nucleotide in sequence
    )


def reverse_complement(sequence: str) -> str:
    """
    Calculate the reverse complement of a DNA sequence.
    """

    sequence = sequence.upper()

    if not validate_sequence(sequence):
        raise ValueError("Invalid or empty DNA sequence.")

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    complementary_sequence = ""

    for nucleotide in sequence:
        complementary_sequence += complement[nucleotide]

    reverse_complement_sequence = complementary_sequence[::-1]

    return reverse_complement_sequence


def calculate_kmers(sequence: str, k: int) -> dict:
    """
    Calculate the frequency of each k-mer in a DNA sequence.
    """

    sequence = sequence.upper()

    if not validate_sequence(sequence):
        raise ValueError("Invalid or empty DNA sequence.")

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    if k > len(sequence):
        raise ValueError("k cannot exceed sequence length.")

    counts = {}

    for start in range(len(sequence) - k + 1):

        kmer = sequence[start:start + k]

        counts[kmer] = counts.get(kmer, 0) + 1

    return counts


def read_fasta(filepath: str) -> dict:
    """
    Read a FASTA file and extract its sequences.

    Returns:
        Dictionary containing headers and DNA sequences.
    """

    sequences = {}
    current_header = None
    current_sequence = ""

    with open(filepath, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                # Save the previous sequence
                if current_header is not None:
                    sequences[current_header] = current_sequence

                # Extract the new header
                current_header = line[1:].strip()

                if not current_header:
                    raise ValueError("FASTA header cannot be empty.")

                current_sequence = ""

            else:

                if current_header is None:
                    raise ValueError(
                        "FASTA sequence found before any header."
                    )

                current_sequence += line.upper()

    # Save the final sequence
    if current_header is not None:
        sequences[current_header] = current_sequence

    return sequences


# Test the functions
if __name__ == "__main__":

    test_sequence = "AAGTCG"

    print("Original sequence:", test_sequence)
    print("Valid sequence:", validate_sequence(test_sequence))
    print("Reverse complement:", reverse_complement(test_sequence))
    print("2-mers:", calculate_kmers(test_sequence, 2))
    print("3-mers:", calculate_kmers(test_sequence, 3))

    print("\nFASTA FILE ANALYSIS")

    fasta_data = read_fasta("data/sample.fasta")

    for header, sequence in fasta_data.items():

        print("\nHeader:", header)
        print("Sequence:", sequence)
        print("Valid:", validate_sequence(sequence))

        if validate_sequence(sequence):
            print("Reverse complement:", reverse_complement(sequence))
            print("2-mers:", calculate_kmers(sequence, 2))
