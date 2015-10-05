''' The Sacred Data Structure '''


''' The big wrapper class for all the objects '''


class Markov:
    def __init__(self, parsed_data):
        self.data = parsed_data                     # Have a lot of properties, maybe clean up later
        # self.openers = Island("OPENER")
        # self.mids = Island("MID")
        # self.finishers = Island("FINISHER")


''' Wrapper for nodes and node types '''


# class Island:
#     def __init__(self, identifier):
#         self.identifier = identifier
#         # self.nodes


''' The node, which also has multiple types '''


class Node:
    def __init__(self, value, node_type):
        self.value = value
        self.type = node_type           # Either is a word (maybe properties later) or punctuation
        # self.island = island            # In case need to reference wrapper
        self.word_links = []
        self.punct_links = []           # Seperate


''' Links need their own class '''


class Link:
    def __init__(self, target):
        self.target = target
        self.target_type = target.type
        self.frequency = 1
        self.previous_words = []        # For later, doesn't have to be used right now


''' The cup weighing, must have cup specific properties '''


class Cup:
    pass
