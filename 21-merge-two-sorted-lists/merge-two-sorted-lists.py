# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        dummy = ListNode()
        new = dummy

        while ( p1 and p2):
            if p1.val < p2.val:
                new.next = p1
                p1 = p1.next
                new = new.next
            
            elif p2.val < p1.val:
                new.next = p2
                p2 = p2.next
                new =new.next
            
            else:
                new.next = p1
                p1=p1.next
                new =new.next

                new.next = p2
                p2 = p2.next
                new = new.next
        
        if p1:
            new.next = p1
        else:
            new.next = p2
        return dummy.next