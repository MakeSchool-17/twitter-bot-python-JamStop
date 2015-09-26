''' Jimmy's awful attempt at making a defaultdict (kind of) from hashtable~ '''
''' Note: Does not fully work yet. '''


from LinkedList import LinkedList


class HashTable():
    def __init__(self, value_type):
        self.buckets = [[] * 8]
        self.data = []
        self.type = value_type
        self.entries = 0

    ''' Very unrefined implementation of load factor management '''
    def update_buckets(self):
        # todo: fixme!
        # if self.entries >= (len(self.buckets) * 0.6):
        #    self.buckets.extend[[][][][][]]
        pass

    def __setitem__(self, key, value):
        # hash_value = hash(key) % len(self.buckets)
        # if buckets[hash_value] is None:
        #     buckets[hash_value] = LinkedList()
        # if buckets[hash_value].find(key) is None:

        print('called set item!')
        pass

    def __getitem__(self, key):
        self.entries += 1
        self.update_buckets()
        hash_value = hash(key) % len(self.buckets)
        if not self.buckets[hash_value]:
            self.buckets[hash_value] = LinkedList()
        if self.buckets[hash_value].find(key) is None:
            if self.type == int:
                self.buckets[hash_value].insert([key, 0])
        return self.buckets[hash_value].find(key).value[1]

if __name__ == '__main__':
    my_table = HashTable(int)
    my_table['testkey'] += 1
    print('whooo python')
