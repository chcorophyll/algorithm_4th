class HashTable(object):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.slots[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while not self.slots[next_slot] is None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while not self.slots[position] is None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __len__(self):
        count = 0
        for item in self.data:
            if not item:
                count += 1
        return count

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

    def delete(self, key):
        position = self.hash_function(key, len(self.slots))
        found = False
        while not self.slots[position] is None and not found:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None

    def __delete__(self, key):
        self.delete()
