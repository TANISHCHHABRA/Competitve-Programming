# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        def dfs(node: TreeNode, curr: int) -> None:
            if not node: return
            nonlocal res

            curr += node.val
            if curr == target:
                res += 1

            res += maps[curr - target]
            maps[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            maps[curr] -= 1

        from collections import defaultdict
        maps = defaultdict(int)
        res = 0

        dfs(root, 0)
        return res
