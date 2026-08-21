# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        begin = None
        dummy = head

        for _ in range(left-1):
            begin = dummy
            dummy = dummy.next

        prev = None
        curr = dummy
        length = right - left + 1
        while length!=0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            length -= 1

        dummy.next = curr

        if begin:
            begin.next = prev
            return head
        
        return prev