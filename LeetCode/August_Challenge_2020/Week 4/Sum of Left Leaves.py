# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,root, side):
            if root is None:
                return
            if not root.left and not root.right:
                if side == -1:
                    self.ans += root.val
            self.recur(root.left,-1)
            self.recur(root.right,1)
                
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        self.recur(root,0)
        return self.ans
