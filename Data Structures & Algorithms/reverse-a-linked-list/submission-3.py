# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            # save next
            tmp = cur.next
            cur.next = prev

            # update prev and cur cur
            prev = cur
            cur = tmp
            
        
        return prev
        