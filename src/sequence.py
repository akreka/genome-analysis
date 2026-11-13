
def validate_sequence(sequence: str) -> bool:
    """
    Check whether a DNA sequence contains only valid nucleotides.

    Valid nucleotides: A, T, G, C

    Args:
        sequence: A DNA sequence.

    Returns:
        True if the sequence is valid, False otherwise.
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

    DNA complementary base pairs:
        A <-> T
        G <-> C

    Args:
        sequence: A DNA sequence containing A, T, G and C.

    Returns:
        The reverse complement, written in the 5' -> 3' direction.

    Raises:
        ValueError: If the sequence is empty or contains invalid characters.
    """

    # 1. Normalize the input
    sequence = sequence.upper()

    # 2. Validate the sequence
    if not validate_sequence(sequence):
        raise ValueError("Invalid or empty DNA sequence.")

    # 3. Define complementary base pairs
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    # 4. Generate the complementary sequence
    complementary_sequence = ""

    for nucleotide in sequence:
        complementary_sequence += complement[nucleotide]

    # 5. Reverse the complementary sequence
    reverse_complement_sequence = complementary_sequence[::-1]

    return reverse_complement_sequence


# Test the functions
if __name__ == "__main__":

    test_sequence = "AAGTCG"

    print("Original sequence:", test_sequence)
    print("Valid sequence:", validate_sequence(test_sequence))
    print("Reverse complement:", reverse_complement(test_sequence))
