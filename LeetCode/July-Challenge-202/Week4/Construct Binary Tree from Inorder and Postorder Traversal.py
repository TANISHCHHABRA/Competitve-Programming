# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return
        indices = {inorder[i]:i for i in range(len(inorder))}
        def dfs(l,r):
            if l > r:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            val_index = indices[val]
            root.right = dfs(val_index+1,r)
            root.left = dfs(l,val_index-1)
            
            return root
            
            
            
        return dfs(0,len(inorder)-1)
