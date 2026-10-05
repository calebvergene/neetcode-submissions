# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path is either longest height or longest left + right
        longest = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal longest
            longest = max(longest, right+left) # this node acts as root

            return max(left, right) + 1 # return longest path including 1 child
        
        dfs(root)
        return longest