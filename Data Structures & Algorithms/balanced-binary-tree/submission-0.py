# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## thought process. give a func root.left and root.right then 
        ## find the max depths of those. then compare. 
        if not root:
            return True
        def findLength(node, depth):
            #base case
            if not node:
                return depth
            
            depth += 1
            dleft = findLength(node.left, depth)
            dright = findLength(node.right, depth)
            return max(dleft, dright)
        
        return abs(findLength(root.left, 0) - findLength(root.right, 0)) < 2