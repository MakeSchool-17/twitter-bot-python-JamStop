''' Time to token marx! '''


import re


class Tokenizer:
    def __init__(self, text):
        self.data = text

    def _marx(self):
        # Todo: fixme
        marx_split = '[] '
        marxer = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
        for line in self.data:
            for word in punct.split(str(line)):
                pass

if __name__ == "__main__":
    t = Tokenizer('hahahaha')
