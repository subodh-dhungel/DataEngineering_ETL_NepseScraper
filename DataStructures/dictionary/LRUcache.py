from collections import OrderedDict

class LRUcache:
    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self,key):
        if key not in self.cache:
            return -1 #cache miss
        self.cache.move_to_end(key) #mark as recently used
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False) #remove the lease recently used item
        self.cache[key] = value
        
lru = LRUcache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print(lru.cache)
lru.get("a")    #access a making it the most recently used
print(lru.cache)   
lru.put("d", 4)     #b is removed last recently used
print(lru.cache)    
lru.get("c")
lru.put("e", 5)
print(lru.cache)