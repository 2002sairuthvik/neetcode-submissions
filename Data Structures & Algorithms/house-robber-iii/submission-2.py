# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        #dp[node] = [skip_max,rob_max]
        dp={}

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            left_skip=dp[node.left][0] if node.left else 0
            left_rob=dp[node.left][1] if node.left else 0
            right_skip=dp[node.right][0] if node.right else 0
            right_rob=dp[node.right][1] if node.right else 0

            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_skip,left_rob)+max(right_rob,right_skip)

            dp[node]=(skip_node,rob_node)
        dfs(root)
        return max(dp[root]) 