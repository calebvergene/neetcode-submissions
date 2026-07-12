# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## first i need to split the list
        ## then reverse last part of list
        ## then zip them 

        ## split list. have a slow and fast pointer. when the fast reaches
        ## the end, then the slow will be at the middle. 
        fast, slow = head, head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            end = slow
            slow = slow.next
        end.next = None
        
        ## now need to reverse last half
        ahead = slow.next
        slow.next = None
        while ahead:
            temp = ahead.next
            ahead.next = slow
            slow = ahead 
            ahead = temp
        
        ## now zip the first half and the reversed other half 
        curr = head
        while curr and slow:
            temp = curr.next
            temp2 = slow.next
            curr.next = slow
            if temp:
                slow.next = temp
            curr = temp
            slow = temp2
        
        
        
