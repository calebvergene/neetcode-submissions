"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.copies = {}

    def createOrReuse(self, node):
        if node in self.copies:
            return self.copies[node]
        else:
            copy = Node(node.val)
            self.copies[node] = copy
            return copy 
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # keep a hash map to store all of the deep copies 
        # then iterate through the given list and new list at the same time

        curr = head

        while curr:
            copy = self.createOrReuse(curr)
            
            if curr.next:
                copy.next = self.createOrReuse(curr.next)
            
            if curr.random:
                copy.random = self.createOrReuse(curr.random)
            
            curr = curr.next
        
        return self.copies[head]
        

