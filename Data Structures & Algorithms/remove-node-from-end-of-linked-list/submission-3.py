# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, end = head, head
        for i in range(n):
            end = end.next
        prev = None
        while end:
            end = end.next
            prev = curr
            curr = curr.next
        
        # remove the node 
        if not prev:
            # then we are removing the head
            head = curr.next
            curr = head
        else:
            prev.next = curr.next  
            curr = curr.next

        return head      