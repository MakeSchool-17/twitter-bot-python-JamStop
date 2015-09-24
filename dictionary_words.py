import sys
import random


macDictionary = open('/usr/share/dict/words', 'r')
words = list(macDictionary)


def random_Dictionary():
    string = ""
    for x in range(int(sys.argv[1])):
        rand_index = random.randint(0, len(words) - 1)
        string += words[rand_index].replace("\n", " ")
    return string

if __name__ == "__main__":
    print(random_Dictionary())
