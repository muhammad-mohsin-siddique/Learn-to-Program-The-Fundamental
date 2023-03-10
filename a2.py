def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)



def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return dna1 > dna2



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_occur = 0

    for char in dna:
        if char in nucleotide:
            num_occur = num_occur + 1

    return num_occur




def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1





def is_valid_sequence(dna):

    '''
    (str) -> bool

    Return if and only if dna have sequence "ATCG"

    >>> is_valid_sequence ("ATCG")
    True
    >>> is_valid_sequence ("GCTA")
    Falsa
    '''
    return dna in "ATCG"


def insert_sequence(dna1, dna2, index):
    '''
    (str, str, int) -> str

    Return the string after add the dna 2 sequence in dna1 at index

    >>> insert_sequence("CCGG","AT",2)
    CCATGG
    >>> insert_sequence("ATC","ACGG",3)
    ATCACGG
    >>> insert_sequence("ATC","ACGG",1)
    AACGGTC

    '''

    return  dna1[0:index] + dna2 + dna1[index:]





def get_complement(dna):

    '''
    (str) -> str

    Return the complement of the dna otherwise

    >>> get_complement ("A")
    T
    >>> get_complement("T")
    A
    >>> get_complement("G")
    C
    >>> get_complement("C")
    G
    '''
    if dna == "A":
        return "T"
    elif dna == "T":
        return "A"
    elif dna == "G":
        return "C"
    elif dna == "C":
        return "G"


def get_complementary_sequence(dna):

    '''
    (str) -> str

    Return the complement sequence of the dna

    >>> get_complementary_sequence("AT")
    TA
    >>> get_complementary_sequence(ATCAG")
    TAGTC
    '''

    complementary_sequence = ""

    for dna_char in dna:
        if dna_char in "ATCG":
             complementary_sequence = complementary_sequence + get_complement(dna_char)

    return complementary_sequence
