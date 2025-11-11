class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        # Uses Python's built-in hash (keys must be hashable)
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value   # update
                return
        self.table[index].append([key, value])  # new pair

    def search(self, key):
        index = self.hash_function(key)  # <- fix: correct indentation
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False

ht = HashTable()
ht.insert("alice", 42)
ht.insert("bob", 17)
print("Alice is stored at: ", ht.search("alice"))   # 42
#ht.delete("bob")
print("Bob is stored at:", ht.search("bob"))     # None
