# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subroot_present = False
        
        def tup_dfs(node, subroot_tuple):
            nonlocal subroot_present
            if not node or subroot_present:
                return None
            
            tup = (tup_dfs(node.left, subroot_tuple), node.val, tup_dfs(node.right, subroot_tuple))
            if subroot_tuple and tup == subroot_tuple:
                subroot_present = True

            return tup
        
        
        
        subroot_tuple = tup_dfs(subRoot, None)
        tup_dfs(root, subroot_tuple)
        return subroot_present


            
            