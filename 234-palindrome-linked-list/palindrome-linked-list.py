# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        curr = node
        prev = None
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev=curr
            curr = next_node
        return prev
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        p1 = head
        p2 = self.reverse(slow)

        while (p2):
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True