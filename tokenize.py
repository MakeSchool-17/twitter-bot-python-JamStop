''' Time to token marx! '''


import re
# from string import punctuation


class Tokenizer:
    def __init__(self, text):
        self.data = text

    def _marx(self):
        # Todo: fixme
        marx_list = []
        marxer = re.compile(r'[\s{}]+'.format(re.escape("#$%&*+/;<=>@[\]^_`{|}~\'")))
        for line in self.data:
            for word in marxer.split(str(line)):
                marx_list.append(word)
        return marx_list

if __name__ == "__main__":
    with open("marx.txt", 'rb') as f:
        t = Tokenizer(f)
        print(t._marx())
