#Although hash tables come built-in in the form of dictionaries in Python,
#here we'll try to implement our own hash table
class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size

    def __str__(self): #As in the array implementation, this method is used to print the attributes of the class object in a dictionary format
        return str(self.__dict__)
    
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned
    
    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        return self.data
    
    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None
    
    def keys(self):
        keyArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                keyArray.append(self.data[i][0][0])
        return keyArray


myHashtTable = HashTable(50)
print(myHashtTable._hash("izhar"))

print(myHashtTable.set("grapes", 10000))
print(myHashtTable.get("grapes"))
print(myHashtTable.set("apple", 10000))
print(myHashtTable.set("oranges", 10000))

print(myHashtTable.keys())