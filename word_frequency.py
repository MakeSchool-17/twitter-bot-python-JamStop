from string import punctuation
from collections import defaultdict
import re
import sys
import operator
#
#
# marx = open('marx.txt', 'r').readlines()
# punct = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))


def wordlist(file_name: str) -> []:
    file = open(file_name, 'r').readlines()
    punct = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
    word_list = []
    for line in file:
        for word in punct.split(line):
            if word != '':
                word_list.append(word.lower())
    return word_list


def histogram(source_text: str):
    histogram = defaultdict(int)
    for word in wordlist(source_text):
        histogram[word] += 1
    return histogram


def unique_words(hist: defaultdict):
    return len(hist.keys())


def frequency(word: str, hist: defaultdict):
    return hist[word]


def average_frequency(hist: defaultdict):
    sum = 0
    for freq in hist.values():
        sum += int(freq)
    return sum/len(hist.values())


def frequency_search(freq: int, hist: defaultdict):
    word = []
    for v, k in hist.items():
        if k == freq:
            word.append(v)
    # print(word)
    return word


if __name__ == "__main__":
    wf_histogram = (histogram(sys.argv[1]))

    frequency_search(1, wf_histogram)
    sorted_hist = sorted(wf_histogram.values())

    ''' Testing~! '''
    print('The most common word(s) is {}, having appeared {} time(s)\nThe least common word(s) is {}, having appeared {} time(s)' \
        .format(frequency_search(sorted_hist[-1], wf_histogram), sorted_hist[-1], \
        frequency_search(sorted_hist[0], wf_histogram), sorted_hist[0]))
    print('There are {} unique words'.format(unique_words(wf_histogram)))
    print('The average frequency of words is {}'.format(average_frequency(wf_histogram)))

    # print (wf_histogram)
    # print (unique_words(wf_histogram))
    # if len(sys.argv) >= 3:
    #     print (frequency(sys.argv[2], wf_histogram))
