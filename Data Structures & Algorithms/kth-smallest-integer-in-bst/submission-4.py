# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        kth = None
        def dfs(node):
            nonlocal kth, count
            if not node or kth:
                return 
            dfs(node.left)
            count += 1
            if count == k:
                kth = node.val
            dfs(node.right)
        dfs(root)
        return kth