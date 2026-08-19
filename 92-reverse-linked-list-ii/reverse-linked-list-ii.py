# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right: return head

        curr_node = head
       
        if left==1:
            before = None
        else:
            for _ in range(left-2):
                curr_node = curr_node.next
            
            before = curr_node 
            curr_node = curr_node.next 
                            

        prev = None
        curr = curr_node

        times = right-left+1

        for _ in range(times):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        curr_node.next = curr 

        if before:
            before.next = prev
            return head
        
        else:
            return prev 
        

