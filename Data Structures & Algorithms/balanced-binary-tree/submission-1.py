# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True,0)

            left_balanced,left_h = dfs(node.left)
            right_balanced,right_h = dfs(node.right)

            balanced = (left_balanced and right_balanced and abs(left_h - right_h)<=1)

            current_h = 1+max(left_h,right_h)

            return (balanced,current_h)

        return dfs(root)[0]