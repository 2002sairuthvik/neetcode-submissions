"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dc = {None:None}

        curr = head
        while curr:
            dc[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            dc[curr].next = dc[curr.next]
            dc[curr].random = dc[curr.random]
            curr = curr.next
        return dc[head]
