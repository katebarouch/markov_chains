"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)
    whole_file = f.read().split()

    f.close()

    return whole_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """


    chains = {}
    
    for word in range(len(text_string)-2):
        
        bigram = (str(text_string[word]), str(text_string[word +1]))
        transitions = text_string[word + 2]

        if bigram in chains:
            chains[bigram].append(transitions)
        else:
            chains[bigram] = [transitions]

        # chains[bigram] = transitions


    for bigram, transition in chains.items():
        print(f"{bigram} {transition}")

    return chains

# make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains):
    """Return text from chains."""

    words = []

    # list_keys = list(chains.keys())

    #first random key + transitions
    
    while True:
        # print(bigram)
        if len(words) == 0:
            bigram_list = list(chains.keys())
            bigram = choice(bigram_list)
            random_key = bigram
            # random_key will always run first bigram
            for word in random_key:
                words.append(word)
            # words.append(random_key)
        else:
            newKey = (words[-2], words[-1])
            if newKey == ('I', 'am?'):
                break
            else:
                transition_list = chains[newKey]
                random_transition = choice(transition_list)
                words.append(random_transition)

    sentence = " ".join(words)
    return sentence
    

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
