# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:        
        # get length first 
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        
        if length == 1 or length == 2:
            return head

        mid = math.ceil(length / 2)
        print(length, mid)
        # break off the chain
        curr = head
        for i in range(mid-1):
            curr = curr.next
        next_start = curr.next
        curr.next = None
        print(next_start.val)

        # reverse last half
        prev = None
        curr = next_start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # zipper combine 
        curr1, curr2 = head, prev
        while curr1 and curr2:                
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1, curr2 = next1, next2
                 
