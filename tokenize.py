''' Time to token marx! '''


import re
from string import punctuation


class Tokenizer:
    def __init__(self, text):
        self.data = text

    def _marx(self):
        # Todo: fixme
        marx_list = []
        marxer1 = re.compile(r'[\s{}]+'.format(re.escape("#$%&*+/;<=>@[\]^_`{|}~\'")))
        # marxer2 = re.compile(r'[({})]+'.format(re.escape(punctuation)))
        for line in self.data:
            for word in marxer1.split(line):
                if word is not '':
                    if word[-1] in punctuation:
                        marx_list.append(word[:-1])
                        marx_list.append(word[-1])
                    else:
                        marx_list.append(word)

        return marx_list
if __name__ == "__main__":
    with open("marx.txt", 'r') as f:
        t = Tokenizer(f)
        print(t._marx())
