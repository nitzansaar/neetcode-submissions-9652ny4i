# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # go through each node in tree1 and check if that node is sameTree
        # as the subroot
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        left_same = self.isSubtree(root.left, subRoot)
        right_same = self.isSubtree(root.right, subRoot)
        return left_same or right_same