# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST so it is sorted from left to right
        # left is always less, right always more

        # if you are at a node and right is >= than q
        # and left is <= p
        # i think that means it is an ancestor so
        # return root


        # yea so basically go down the tree until you reach a fork
        # then return that node
        cur = root
        while cur:
            # either move left or right
            if cur.val > q.val and cur.val > p.val:# move left
                cur = cur.left
            elif cur.val < q.val and cur.val < p.val:
                cur = cur.right
            else:
                return cur
        return root

            
            