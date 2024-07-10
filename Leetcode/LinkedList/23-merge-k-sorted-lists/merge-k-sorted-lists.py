# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time - O(n * logk)
    # divide & conquer
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     l,r = self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:])
    #     return self.merge(l,r)
    
    # def merge(self,l,r):
    #     dummy = p = ListNode(0)
    #     while l and r:
    #         if l.val < r.val:
    #             p.next = l
    #             l = l.next
    #         else:
    #             p.next = r
    #             r = r.next
    #         p = p.next
    #     p.next = l or r
    #     return dummy.next

    # using min heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # from heapq import heappush,heappop
        # heapp = []
        # for nodes in lists:
        #     if nodes:
        #         heappush(heapp,(nodes.val,nodes))

        # dummy = p = ListNode(0)
        # while len(heapp) > 0:
        #     node = heappop(heapp)
        #     p.next = node
        #     p = p.next
        #     if node.next:
        #         heappush(heapp,(node.next.val,node.next))

        # return dummy.next

        heapp = []
        for nodes in lists:
            while nodes:
                heappush(heapp, nodes.val)
                nodes = nodes.next

        dummy = p = ListNode(0)
        while heapp:
            val = heappop(heapp)
            p.next = ListNode(val)
            p = p.next

        return dummy.next
        