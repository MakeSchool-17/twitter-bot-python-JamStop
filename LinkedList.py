''' LinkedList implementation '''


import Node


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current, counter = self.head, 0
        while current:
            counter += 1
            current = current.next
        return counter

    def find(self, key):
        current = self.head
        while current:
            if current.key == value:
                return current
            else:
                current = current.next
        return None

    # def remove(self, value):
