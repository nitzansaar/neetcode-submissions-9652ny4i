# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # go through each node in the tree and find the max depth in both directions
        # for that node 
        # keep a global variable for the max diameter which is the sum of 
        # max depth in both directions
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            self.res = max(self.res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        dfs(root)
        return self.res