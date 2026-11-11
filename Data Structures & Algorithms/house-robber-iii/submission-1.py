# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def dfs(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]

            rob_curr=root.val
            if root.left:
                rob_curr += dfs(root.left.left)+dfs(root.left.right)
            if root.right:
                rob_curr +=dfs(root.right.left)+dfs(root.right.right)

            skip_curr = dfs(root.left)+dfs(root.right)
            memo[root]=max(rob_curr,skip_curr)
            return memo[root]
        return dfs(root)
        