# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # space - O(N/k)

        # curr = head
        # cnt = 0
        # while cnt < k:
        #     if curr is None:
        #         return head
        #     curr = curr.next
        #     cnt += 1

        # nxtList = self.reverseKGroup(curr,k)
        # while cnt > 0:
        #     temp = head.next
        #     head.next = nxtList
        #     nxtList = head
        #     head = temp
        #     cnt -= 1
        
        # return nxtList

        # space optimal - O(1)
        dummy = ListNode(0)
        dummy.next = head
        temp = head
        currHead = head
        cnt = 1
        prevList = dummy  # Initialize prevList to dummy node
        while temp:
            while cnt < k:
                if temp.next is None:
                    break
                temp = temp.next
                cnt += 1
            if temp.next is None and cnt < k:  # If remaining nodes are less than k
                break
            nextNode = temp.next
            temp.next = None
            newHead = self.revers(currHead)
            prevList.next = newHead  # Connect the previous sublist to the new head
            currHead.next = nextNode
            prevList = currHead
            currHead = nextNode
            temp = nextNode
            cnt = 1

        return dummy.next

    def revers(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev



