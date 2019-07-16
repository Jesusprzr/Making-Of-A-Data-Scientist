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
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    occurrences = 0
    for char in dna:
        if char in nucleotide:
            occurrences = occurrences + 1
    return occurrences
    
    
def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna_sequence):
    ''' (str) -> bool
    Returns whether dna_sequence is a valid or non valid 
    dna sequence. If valid returns True, if non valid returns False.

    >>> is_valid_sequence('ATGC')
    >>> True
    >>> is_valid_sequence('ATGCAC')
    >>> True
    >>> is_valid_sequence('aTGc')
    >>> False
    >>> is_valid_sequence('ATGCK')
    >>> False
    '''
    
    if dna_sequence == '':
        dna_sequence = 'z'
    invalid_chars = 'BDEFHIJKLMNÑOPQRSUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789'
    if set(invalid_chars).intersection(dna_sequence):
        return False
    else:
        return True
    
#THIS IS NOT TRUE AT ALL, BECAUSE HAD TO SEACH ONLINE FOR A WAY TO SOLVE IT, AND WASN'T SOMETHING I KNEW
#I WAS REALLY STUCKED ON THIS ONE, BUT FINALLY MADE IT!!
#The problem as always, was simple but not so obvious
#I tried every different combiination that i knew, even the one of the solution
#but any combination of code worked. This one works because first it takes every word
#sepparatedly and then it sees of the word was any of the above, if not it adds +1 to false_seq
#I used this code before, but instead of 'AGCT' i was using 'A' or 'C' or 'T' or 'G' and it 
#wasn't working at all... Gotta whatch on the py viz why that doesn't work.

def insert_sequence(seq1 , seq2, index):
    ''' (str, str, int) -> str

    Return the dna sequence obtained by 
    inserting seq2 in seq1 at index.
    >>> insert_sequence('ACGAT', 'CTG', 3)
    ACGCTGAT
    >>> insert_sequence('ACC', 'TGA', 2)
    ACTGAC
    '''
    return seq1[:index] + seq2 + seq1[index:]

def get_complement(nucleotide):   
    '''(str) -> str
    
    Returns the given nucleotide's complementary nucleotid.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    '''
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    else:
        return False


def get_complementary_sequence(nsequence):
    '''(str) -> str

    Returns the complementary sequence of nsequence nucleotides sequence.

    >>> get_complementary_sequence('AC')
    >>> 'TG'
    >>> get_complementary_sequence('AT')
    >>> 'TA'
    '''
    c_seq = ''
    for char in nsequence:
        if char in 'A':
            c_seq = c_seq + 'T'
    for char in nsequence:
        if char in 'C':
            c_seq = c_seq + 'G'
    for char in nsequence:
        if char in 'T':
            c_seq = c_seq + 'A'
    else:
        if char in 'G':
            c_seq = c_seq + 'C'
    
        return c_seq

#Some tests failed:
#[TestIsValidSequence] False is not true : Have you tested your function with a zero-length sequence?  (It should be valid.)
#[TestGetComplementarySequence] 'TTGGAAC' != 'TAGCTAGC'
#- TTGGAAC
#+ TAGCTAGC
# : Have you tested your function on a sequence with multiple occurrences of each nucleotide?
#[TestGetComplementarySequence] Your code raised an unexpected exception: local variable 'char' referenced before assignment