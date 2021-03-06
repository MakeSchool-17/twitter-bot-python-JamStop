''' Jimmy MaxHeap '''


class MaxHeap:
    def __init__(self):
        self.data = [None]
        self.size = 0

    ''' Percolate up in order to move an appended index to the right place '''
    def percolate_up(self, index):
        while index // 2 > 0:                               # work way up to root
            if self.data[index] > self.data[index // 2]:    # check if we still need to move
                value = self.data[index // 2]               # keep track of what we're moving
                self.data[index // 2] = self.data[index]    # move our item up
                self.data[index] = value                    # switch the other one in
            index = index // 2                              # we move up the heap

    ''' Percolate down in order to reset a heap to proper structure '''
    def percolate_down(self, index):
        while index * 2 <= self.self.size:                  # Check if we still have room to move down
            maximum = self.get_max_child(index)             # Find the node's maximum child
            if self.data[index] < self.data[maximum]:       # Check if we have reached the bottom
                temp = self.data[index]                     # Keep track before switch
                self.data[index] = self.data[maximum]       # Switch node
                self.data[maximum] = temp                   # Switch node
            index = maximum                                 # move our location downwards

    def insert(self, value):
        self.data.append(value)
        self.size += 1
        self.percolate_up

    def build(self, data):
        self.size = len(data)
        d_index = len(data) // 2
        self.data = [0] + data[:]
        while d_index > 0:
            self.percolate_down(d_index)
            d_index -= 1

    ''' Deletes the maximum (root) in the heap '''
    def delete_minimum(self):
        value = self.data[1]
        self.data[1] = self.data[self.size]
        self.size -= 1
        self.data.pop()
        self.percolate_down(1)
        return value

    ''' Find the max child of the current sample node '''
    def get_max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.data[index * 2] > self.data[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
