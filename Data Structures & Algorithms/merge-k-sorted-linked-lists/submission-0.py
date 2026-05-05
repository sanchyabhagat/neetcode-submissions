# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # basic edge case
        if not lists or len(lists) == 0:
            return None
        
        # Merge pairs of lists till we only have pone left
        while len(lists) > 1:
            resultLists = []
            # Iterate in steps of 2 for the entire length of linkedlists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # edge case 2 - reached end of lists
                l2 = lists[i+1] if (i+1) < len(lists) else None
                resultLists.append(self.mergeTwoLists(l1, l2))
            # update our main lists with the merge ones and repeat
            lists = resultLists
        return lists[0]

    # Helper function to merge two sorted lists
    def mergeTwoLists(self, list1, list2) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        
        elif list2:
            tail.next = list2
        
        return dummy.next