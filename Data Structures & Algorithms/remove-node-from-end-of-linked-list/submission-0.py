# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sample = []
        cur = head

        while cur:
            sample.append(cur)
            cur = cur.next
        
        rem = len(sample) - n
        # print(rem)

        if rem == 0:
            return head.next

        sample[rem-1].next = sample[rem].next
        return head
