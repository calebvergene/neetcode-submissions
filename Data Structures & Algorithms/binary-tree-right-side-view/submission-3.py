# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        right_side = []
        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if curr.left: 
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == length - 1:
                    right_side.append(curr.val)
        return right_side