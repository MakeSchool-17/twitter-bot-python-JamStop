''' The Sacred Data Structure '''


''' The big wrapper class for all the objects '''


from collections import defaultdict
from string import punctuation


class Markov:
    def __init__(self, parsed_data):                # Parsed data that is passed in is split into words and punct
        self.data = parsed_data                     # Have a lot of properties, maybe clean up later
        # self.openers = Island("OPENER")
        # self.mids = Island("MID")
        # self.finishers = Island("FINISHER")

        self.openers = defaultdict(Node)
        self.mids = defaultdict(Node)
        self.finishers = defaultdict(Node)

    def build(self):
        prev_node = None                            # Keep track of previous node for markov purposes
        state = "START"                                # Keep track of the state the parser is in
        for index in range(self.data):
            new_node = None
            item = self.data[index]
            if index == 0:
                new_node = Node(item, "START")
                self.openers.add(new_node)
                prev_node = new_node
                state = "MID"
            else:                                   # Bulk of checkers in here
                if state == "MID":
                    if item in punctuation:
                        new_node = Node(item, "PUNCT")
                        previous_node.punct_links.append(Link())


''' Wrapper for nodes and node types '''


# class Island:
#     def __init__(self, identifier):
#         self.identifier = identifier
#         # self.nodes


''' The node, which also has multiple types '''


class Node:
    def __init__(self, value, node_type):
        self.value = value
        ''' NODE TYPES: START, MID, END, MID_PUNCT, END_PUNCT '''
        self.type = node_type           # Either is a word (maybe properties later) or punctuation
        # self.island = island            # In case need to reference wrapper
        self.word_links = defaultdict(Link)            # Need seperate data structure instead of lists for link
        self.punct_links = defaultdict(Link)           # Seperate


''' Links need their own class '''


class Link:
    def __init__(self, target):
        self.target = target
        self.target_type = target.type
        self.frequency = 0
        self.previous_words = []        # For later, doesn't have to be used right now


''' The cup weighing, must have cup specific properties '''


class Cup:
    pass
