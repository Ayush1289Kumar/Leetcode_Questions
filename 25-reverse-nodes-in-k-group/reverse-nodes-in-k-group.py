# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node,size):
        curr = node
        prev = None

        for _ in range(size):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head

        left = head
        ans = None
        prevLeft = None
        nextLeft =None
        right = None
        size = k

        while(True):
            right = left
            for _ in range(size-1):
                if not right:
                    break
                right=right.next
            
            if right:
                nextLeft = right.next
                self.reverse(left,size)
                if prevLeft:
                    prevLeft.next = right
                prevLeft = left

                if ans == None:
                    ans = right
                
                left = nextLeft
            
            else:
                if prevLeft:
                    prevLeft.next = left

                if ans == None:
                    ans = left
                break
        return ans

        