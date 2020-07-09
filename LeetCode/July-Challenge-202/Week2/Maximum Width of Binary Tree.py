# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        '''
        
        Brute Force BFS; generating all levels inclusive of None and
        then iterating each to find the first and last element and returning the max difference between right and left;
        This is TLE
        '''
        '''
        queue = []
        queue.append(root)
        ans = []
        ans.append(None)
        res = 0
        while any(queue):
            
            leftmost, rightmost = float('inf'), float('-inf')
            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if not curr:   #if not curr add left None and right
                    ans.append(None)
                    queue.append(None)
                    queue.append(None)
                elif curr:
                    ans.append(curr)
                    if curr.left:
                        leftmost = min(leftmost, 2 * ans.index(curr))
                        rightmost = max(rightmost, 2 * ans.index(curr))
                        queue.append(curr.left)
                    else:
                        queue.append(None)
                    if curr.right:
                        leftmost = min(leftmost, (2 * ans.index(curr)) + 1)
                        rightmost = max(rightmost, (2 * ans.index(curr)) + 1)
                        queue.append(curr.right)
                    else:
                        queue.append(None)
                        
            
            res = max(res, rightmost - leftmost + 1)
            
            
            
        
        if res == 0:
            return 1
        return res
        '''
        
        queue = [(root, 1)]
        ans = 1
        
        while queue:
            if len(queue) > 1:
                ans = max(queue[-1][1] - queue[0][1] + 1, ans)
            
            temp = []
            while queue:
                node, level = queue.pop(0)
                if node.left:
                    temp.append((node.left, 2 * level))
                if node.right:
                    temp.append((node.right, 2 * level + 1))
            queue = temp
        return ans
