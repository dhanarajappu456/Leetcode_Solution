# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        
        ans  =[]


        def rec(root):

            if root == None:
                return None 

            rec(root.left)

            ans.append(root.val)

            rec(root.right)
       
        rec(root)

        return ans 