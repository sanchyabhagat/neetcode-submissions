class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to Node

        # left = LRU and right = most recent
        self.left, self.right = Node(0,0), Node(0,0)
        # intiially linked to each other, no other nodes
        self.left.next, self.right.prev = self.right, self.left
        
    ## Remove node from cache - 
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node to cache - 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from LRU
            self.remove(self.cache[key])        
            # add to most recent
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        
        # check if key is already in cache and remove
        if key in self.cache:
            self.remove(self.cache[key])
        # add to cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
