# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder shows left to right
        # preorder shows top to bottom

        # so start at root
        # for each node, NEED TO find its children. focus on this small task for dfs.
            # for in order, its left will be its parent/leftchild and its right will be its right child
            # to tell if its parent/leftchild, look in preorder to see what level its in 

        # make dict of indices for O(1) lookup of positioning
        pre = collections.defaultdict(int)
        post = collections.defaultdict(int)
        for i in range(len(preorder)):
            pre[preorder[i]] = i
            post[postorder[i]] = i

        def dfs(val):
            pre_index = pre[val]
            post_index = post[val]
            node = TreeNode(val)
            # find left children
            # while loop until you find the nearest node below and to the left 
            left = pre_index
            while left < len(preorder):
                check = preorder[left]
                if post[check] < post:
                    # FOUND! this node is below and to the left
                    # remove from dicts when done, dont want to reuse
                    del pre[check]
                    del post[check]
                    node.left = dfs(check)
                    
                left += 1
            if left >= len(preorder):
                node.left = None

            return node
