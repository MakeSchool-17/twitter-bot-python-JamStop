import random
import sys
import word_frequency
from collections import defaultdict


def random_word(wordlist: list):
    return random.choice(wordlist)


''' Testing~! '''


def test(file_name: str):
    counter = defaultdict(int)
    for i in range(10000):
        word = random_word(file_name)
        counter[word] += 1
    return sorted(counter.items(), key=lambda wfreq: wfreq[1])


if __name__ == "__main__":
    wordlist = word_frequency.wordlist(sys.argv[1])
    print(test(wordlist))
