# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        
        def dfs(node):
            if not node:
                return False, False
            lp_seen, lq_seen = dfs(node.left)
            rp_seen, rq_seen = dfs(node.right)
            p_seen = node == p or lp_seen or rp_seen
            q_seen = node == q or lq_seen or rq_seen
            if p_seen and q_seen:
                nonlocal lca
                if not lca:
                    lca = node
            return p_seen, q_seen
        
        dfs(root)
        return lca
            