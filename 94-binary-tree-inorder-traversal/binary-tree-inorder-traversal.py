# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        
        stk = []
        ans  =  []
        while(stk or root):


            while(root):
                stk.append(root)
                root = root.left
            top = stk.pop(-1)
            ans.append(top.val)

            root = top.right
        return ans 