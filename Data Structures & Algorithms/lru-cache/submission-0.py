class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  #map keys to Node
        
        # left - LRU , right - MRU(most recently used)
        self.left,self.right = Node(0,0) , Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # removes from the list    
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev    
    #adds from the right
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    
    def get(self, key: int) -> int:
        if key in self.cache:
            # we have to update the left and right so we are correctly on lru and MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            # remove from list and delete lru from from hashmap
            lru = self.left.next
            self.remove(lru)
            del(self.cache[lru.key])
        
