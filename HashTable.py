class HashTable:
    def __init__(self):
        self.data = []


    def get(key, asoc_array):
        # The less efficient, list based version:
        # for index, value in enumerate(asoc_array):
        #     if value == key:
        #         return asoc_array[index + 1]
        # return None


        # Hashing!
        
