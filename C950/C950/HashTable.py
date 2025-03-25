
class HashTable:
    # constructor
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # inserting new values to hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def getValue(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]