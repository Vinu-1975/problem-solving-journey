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
        hashie = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            hashie[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = hashie[curr]
            copy.next = hashie[curr.next]
            copy.random = hashie[curr.random]
            curr = curr.next

        return hashie[head]