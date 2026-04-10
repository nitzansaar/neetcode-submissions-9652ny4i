# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check if at any node in the tree, the depths of the left and right childs 
        # vary by more than 1
        # if so, return false
        # if you make it through the entire tree, return true
        self.balanced = True

        def dfs(node):
            if not node or not self.balanced:
                return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            if abs(leftDepth - rightDepth) > 1:
                self.balanced = False
            return 1 + max(leftDepth, rightDepth)

        dfs(root)
        return self.balanced