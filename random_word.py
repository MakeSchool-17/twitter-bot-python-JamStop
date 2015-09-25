import random
import sys
import word_frequency
from collections import defaultdict


def get_wordlist():
    return word_frequency.wordlist(sys.argv[1])


def random_word(wordlist: list):
    return random.choice(wordlist)


''' Testing~! '''
''' Side Note! To increase weight for a word just add more to the wordlist! '''


def test(wl: list):
    counter = defaultdict(int)
    for i in range(10000):
        word = random_word(wl)
        counter[word] += 1
    return sorted(counter.items(), key=lambda wfreq: wfreq[1])


if __name__ == "__main__":
    wordlist = get_wordlist()
    print(test(wordlist))
