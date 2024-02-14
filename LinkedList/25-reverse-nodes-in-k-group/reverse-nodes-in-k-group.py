# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while cnt < k:
            if curr is None:
                return head
            curr = curr.next
            cnt += 1

        nxtList = self.reverseKGroup(curr,k)
        while cnt > 0:
            temp = head.next
            head.next = nxtList
            nxtList = head
            head = temp
            cnt -= 1
        
        return nxtList