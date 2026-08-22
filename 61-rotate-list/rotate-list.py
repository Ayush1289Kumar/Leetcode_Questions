# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        last = head
        n = 1

        while last.next:
            last = last.next
            n+=1
        
        k=k%n
        if not k:
            return head
        
        cnt = 1
        dummy = head

        while dummy:
            if (cnt == (n-k)):
                break
            cnt+=1
            dummy = dummy.next

        last.next = head
        ans = dummy.next
        dummy.next = None

        return ans

        