''' Jimmy's Attempt at Heaps :D '''


class Heap:
    def __init__(self):
        self.data = [None]
        self.size = 0

    def percolate(self, size):
        while size // 2 > 0:
            if self.data[size] > self.data[size // 2]:
                value = self.data[size // 2]
                self.data[size // 2] = self.data[size]
                self.data[size] = value
