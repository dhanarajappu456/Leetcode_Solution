# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def rec(root,li):

            if root == None: 
                return 
            if  root.left == None and  root.right==None:
                li.append(root.val)
            rec(root.left,li)
            rec(root.right,li)
        l1,l2 = [], []
        rec(root1,l1)
        rec(root2,l2)

        return l1==l2