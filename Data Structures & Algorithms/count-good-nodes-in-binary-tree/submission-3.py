# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, largest_above):
            if not node:
                return 
            nonlocal good
            if node.val >= largest_above:
                good += 1
                largest_above = node.val
            dfs(node.left, largest_above)
            dfs(node.right, largest_above)

        dfs(root, -101)
        return good