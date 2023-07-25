"""
Description: Hash Table - store strings using hashing.

"""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hc = self.compute_hash_codes(string)
        if hc != -1:
            if self.table[hc] is not None:
                self.table[hc].append(string)
            else:
                self.table[hc] = [string]

    def lookup(self, string):
        hc = self.compute_hash_codes(string)
        if hc != -1:
            if self.table[hc] is not None:
                if string in self.table[hc]:
                    return hc
        return -1

    @staticmethod
    def compute_hash_codes(string):
        hash_code = ord(string[0]) * 100 + ord(string[1])
        return hash_code


# Test cases
hash_table = HashTable()
s = 'Algorithms'
# should print 6608
print(hash_table.compute_hash_codes(s))
hash_table.store('Algorithms')
print(hash_table.lookup('Algorithms'))
