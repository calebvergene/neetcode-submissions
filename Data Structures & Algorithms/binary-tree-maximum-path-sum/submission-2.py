# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # each root has a max path. 
        # each node pass back its maximum path below it. 
        # then root calcs path with l + r
        max_path = float('-inf')

        def dfs(node):
            if not node: 
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            # check if we have the max path 
            nonlocal max_path
            max_path = max(max_path, node.val + left + right)

            return max(left+node.val, right+node.val, 0)
        
        dfs(root)
        return max_path
