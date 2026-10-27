      
class MyHashMap:

    def __init__(self):
        self.num_buckets=1098
        self.buckets = [[] for _ in range((self.num_buckets))]

    def _hash(self, key:int) -> int:
        return key%self.num_buckets
        
    def put(self, key: int, value: int) -> None:
        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]
        #updating existing
        for pair in bucket:
            if pair[0]==key:
                pair[1]=value
                return
        #adding new pair
        bucket.append([key,value])

    def get(self, key: int) -> int:

        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]

        # returning value for existing key
        for pair in bucket:
            if pair[0]==key:
                return pair[1]
        
        #if key doesn't exist 
        return -1
        

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]

        for i,pair in enumerate(bucket):
            if pair[0]==key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)