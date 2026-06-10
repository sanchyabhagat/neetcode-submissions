# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # algo
        # 1. while list > 1 elemnts
        # for through pairs of two lists (with edge case checking)
        # merge said lists i.e. sort them
        # update list = mergedResLists after every iteration
        # at the end we will have just one list

        if not lists:
            return None
        
        while len(lists) > 1:
            resList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]

                list2 = lists[i+1] if i+1 < len(lists) else None

                resList.append(self.mergeTwoLists(list1, list2))
            
            lists = resList
        
        return lists[0]

    def mergeTwoLists(self, list1, list2) -> ListNode:
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1 and list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                
                tail = tail.next
            
            if list1:
                tail.next = list1
            
            if list2:
                tail.next = list2
            
            return dummy.next