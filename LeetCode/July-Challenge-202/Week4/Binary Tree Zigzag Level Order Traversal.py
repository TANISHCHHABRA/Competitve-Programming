# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root is None: 
            return ans
        queue = [] 
        queue.append(root)
        ltr = False
        while len(queue) > 0: 
            temp = []
            s = len(queue)
            for i in range(s):
                n = queue.pop(0)
                if ltr:
                    temp.insert(0,n.val)
                else:
                    temp.append(n.val)
                if(n.left != None):
                    queue.append(n.left)
                if(n.right != None):
                    queue.append(n.right)
            ans.append(temp)
            ltr = not ltr
        return ans
