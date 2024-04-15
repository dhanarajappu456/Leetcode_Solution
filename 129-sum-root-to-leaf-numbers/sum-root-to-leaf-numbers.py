# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:



        def rec(num ,root):

            if root ==None :
                return 0 
            num = num*10 + root.val 
            if root.left==None and root.right ==None:
                return num

            return rec(num , root.left) +  rec(num ,root.right)

        return rec(0,root)