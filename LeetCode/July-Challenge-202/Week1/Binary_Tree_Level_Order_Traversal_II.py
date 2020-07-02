# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        ans = []
        Q = []
        level = 0
        Q.append(root)
        
        while Q:
            ans.append([])
            for _ in range(len(Q)):
                s = Q.pop(0)
                ans[level].append(s.val)
                
                if s.left:
                    Q.append(s.left)
                if s.right:
                    Q.append(s.right)
                    
            level += 1
        ans.reverse()
        return ans
