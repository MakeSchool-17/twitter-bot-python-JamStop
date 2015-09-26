''' LinkedList implementation '''


# import Node
from Node import Node

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
            if current.value[0] == key:
                return current
            else:
                current = current.next
        return None

    def remove(self, key):
        current = self.head
        previous = None
        while current:
            if current.value == key:
                if previous is None:
                    self.head = current.next
                    return
                previous.next = current.next
                return
            previous = current
            current = current.next
        return
