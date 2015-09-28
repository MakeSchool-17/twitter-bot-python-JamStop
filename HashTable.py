''' Jimmy's awful attempt at making a defaultdict (kind of) from hashtable~ '''
''' Note: Does not fully work yet. '''
''' Note2: My linkedlist implementation isn't amazing, so it's been leaking
    into this hashtable implementation '''


from LinkedList import LinkedList


class HashTable():
    def __init__(self, value_type):
        self.buckets = [[] * 5000]
        self.data = []
        self.type = value_type
        self.entries = 0

    ''' Very unrefined implementation of load factor management '''
    def update_buckets(self):
        # todo: fixme!
        if self.entries >= (len(self.buckets) * 0.6):
            self.buckets.extend([] * 5)

    def __setitem__(self, key, value):
        self[key]
        hash_value = hash(key) % len(self.buckets)
        target = value
        # print (value)
        # print(target)
        if type(target) is int and type(value) is int:
            self.buckets[hash_value].find(key).value[1] += target
        return target

    def __getitem__(self, key):
        hash_value = hash(key) % len(self.buckets)
        if not self.buckets[hash_value]:
            self.buckets[hash_value] = LinkedList()
            self.entries += 1
            self.update_buckets()
        if self.buckets[hash_value].find(key) is None:
            if self.type == int:
                self.buckets[hash_value].insert([key, 0])
        return self.buckets[hash_value].find(key).value[1]

    def __len__(self):
        return self.entries

    # def __del__(self, key):
    #     hash_value = hash(key) % len(self.buckets)
    #     if self.buckets[hash_value].find(key):
    #         self.buckets[hash_value].remove(key)
    #         self.entries -= 1
    #         self.update_buckets()
    #     else:
    #         raise KeyError('{} not found'.format(key))

if __name__ == '__main__':
    my_table = HashTable(int)
    print(my_table['testkey'])      # before mutation
    my_table['testkey'] += 5
    print(my_table['testkey'])      # check if value was properly set
    my_table['otherkey'] = 2
    print(my_table['otherkey'])     # check direct setting

    print('whooo python')
