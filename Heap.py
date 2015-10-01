''' Jimmy's Attempt at Heaps :D '''


class Heap:
    def __init__(self):
        self.data = [None]
        self.size = 0

    ''' Percolate up in order to move an appended index to the right place '''
    def percolate_up(self, index):
        while index // 2 > 0:                               # work way up to root
            if self.data[index] < self.data[index // 2]:    # check if we still need to move
                value = self.data[index // 2]               # keep track of what we're moving
                self.data[index // 2] = self.data[index]    # move our item up
                self.data[index] = value                    # switch the other one in
            index = index // 2                              # we move up the heap

    ''' Percolate down in order to reset a heap to proper structure '''
    def percolate_down(self, index):
        while index * 2 <= self.self.size:


    def insert(self, value):
        self.data.append(value)
        self.size += 1
        self.percolate_up

    def get_min_child(self, index):                                 #
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.data[index * 2] < self.data[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
