class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next: "ListNode" = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.capacity = 10007
        # Initialize each bucket with a dummy head node
        self.buckets = [ListNode() for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value  # Key exists, update value
                return
            curr = curr.next
        # Key does not exist, append at the end
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.buckets[self._hash(key)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Unlink target node
                return
            curr = curr.next