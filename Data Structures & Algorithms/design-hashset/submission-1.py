class ListNode:
    def __init__(self, key: int = -1, next: "ListNode" = None):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        # Using a prime number to reduce modulo collision clustering
        self.capacity = 10007
        # Each bucket contains a dummy head node
        self.buckets = [ListNode() for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                return  # Key already exists
            curr = curr.next
        # Append new node at tail
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Unlink the node
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False