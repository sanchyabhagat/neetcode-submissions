# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first half as is
        # second half reversed list
        # merge first half and second half
        # need to find middle of list usign slow/fast pointers

        ## find first and second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # do the calculation, when fast reaches end,
        # slow.next will be second half
        second = slow.next
        # break off first half and second half
        slow.next = None

        # Reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge first half and Reversed-second-half
        # start at first and second half
        first, second = head, prev
        # second half can be shorter or equal, so this covers both pointers
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # move pointers forward
            first = tmp1
            second = tmp2






