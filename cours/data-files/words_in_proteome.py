"""Find English words in proteome."""

__authors__ = ("Pierre Poulain", "Patrick Fuchs")
__version__ = "1.0.0"
__date__ = "2018-11-23"
__license__ = "BSD 3-Clause"

import sys


def read_words(filename):
    """Read words from file.

    Parameters
    ----------
    filename : str
        Name of file that contains words.

    Returns
    -------
    list
        List of words.

    """
    word_list = []
    with open(filename, "r") as f_in:
        for line in f_in:
            word = line.strip()
            if len(word) >= 3:
                word_list.append(word.upper())
    return word_list


def read_sequences(filename):
    """Read sequences from fasta file.

    Parameters
    ----------
    filename : str
        Name of file that contains sequences in Fasta format.

    Returns
    -------
    dict
        Dictionnary with protein identifier as key and sequence as value.

    """
    prot_dict = {}
    with open(filename, "r") as f_in:
        prot_id = ""
        for line in f_in:
            if line.startswith(">"):
                prot_id = line.split("|")[1]
                prot_dict[prot_id] = ""
            else:
                prot_dict[prot_id] += line.strip()
    return prot_dict


def search_words_in_proteome(word_list, prot_dict):
    """Search and counts words in proteome sequences.

    Parameters
    ----------
    word_list : list
        List of words.
    prot_dict : dict
        Dictionnary of proteins with identifier as key and sequence as value.

    Returns
    -------
    dict
        Dictionnary of words with word as key and occurence as value.

    """
    found_word_dict = {}
    for word in word_list:
        seq_count = 0
        for prot_id in prot_dict:
            if word in prot_dict[prot_id]:
                seq_count += 1
        if seq_count != 0:
            found_word_dict[word] = seq_count
            print(f"{word} found {seq_count} in sequences")
    return found_word_dict


def find_most_frequent_word(freq_dict):
    """Find and print the most frequent word found in sequences.

    Parameters
    ----------
    freq_dict : dict
        Dictionnary of words with word as key and occurence as value.

    """
    maxi = max(freq_dict.values())
    for word in freq_dict:
        if freq_dict[word] == maxi:
            print(f"=> {word} found in {maxi} sequences")


if __name__ == "__main__":
    WORDS_FILENAME = sys.argv[1]
    WORDS_LIST = read_words(WORDS_FILENAME)
    print(f"{len(WORDS_LIST)} words found")
    PROTEOME_FILENAME = sys.argv[2]
    PROTEOME = read_sequences(PROTEOME_FILENAME)
    print(f"{len(PROTEOME)} sequences read")
    WORDS_FOUND = search_words_in_proteome(WORDS_LIST, PROTEOME)
    find_most_frequent_word(WORDS_FOUND)
