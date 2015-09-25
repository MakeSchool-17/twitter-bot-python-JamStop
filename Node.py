''' Node implementation '''


class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    #
    # def value(self):
    #     return self.value
    #
    # def next(self):
    #     return self.next

    def set_next(self, next_node):
        self.next = next_node
