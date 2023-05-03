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


def make_chains(text_string, n_input):
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
    """
    [-2,-1]
    [-n::]
    """

    chains = {}
    n = int(n_input)
    for word in range(len(text_string)-n):
        
        # trigram = (str(text_string[word]), str(text_string[word + 1], str(text_string[word + 2])))
        n_gram = []
        for i in range(word, word + n):
            n_gram.append(str(text_string[i]))
        n_gram = tuple(n_gram)
        transitions = text_string[word + n]

        if n_gram in chains:
            chains[n_gram].append(transitions)
        else:
            chains[n_gram] = [transitions]

    
    for n_gram, transition in chains.items():
        print(f"{n_gram} {transition}")
    
    return chains

# make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains, n_input):
    """Return text from chains."""

    words = []
    n = int(n_input)
    # list_keys = list(chains.keys())

    #first random key + transitions
    
    while True:
        
        if len(words) == 0:
            n_gram_list = list(chains.keys())
            n_gram = choice(n_gram_list)
            random_key = n_gram
            
            for word in random_key:
                words.append(word)
            
        else:
            newKey = tuple(words[-n::])
            if words[-3::] == ['from', 'the', 'earth.']:
                break
            else:
                transition_list = chains[newKey]
                random_transition = choice(transition_list)
                words.append(random_transition)

    sentence = " ".join(words)
    return sentence
    

input_path = 'gettysburg.txt'
n_input = input("Enter a number between 2 and 5: ")
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_input)

# Produce random text
random_text = make_text(chains, n_input)

print(random_text)
