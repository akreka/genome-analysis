
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
    valid_nucleotides = {"A", "T", "G", "C"}

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide: {nucleotide}")

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


# Test the function
if __name__ == "__main__":

    test_sequence = "AAGTCG"

    result = reverse_complement(test_sequence)

    print("Original sequence:", test_sequence)
    print("Reverse complement:", result)
    