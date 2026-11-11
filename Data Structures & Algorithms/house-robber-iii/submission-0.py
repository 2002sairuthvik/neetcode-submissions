# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return pair of values [withroot,without_root]
        def dfs(root):
            if not root:
                return [0,0]
            
            left_rob,left_skip=dfs(root.left)
            right_rob,right_skip=dfs(root.right)

            withRoot=root.val+left_skip+right_skip
            withOutRoot=max(left_rob,left_skip)+max(right_rob,right_skip)

            return [withRoot,withOutRoot]
        
        return max(dfs(root))