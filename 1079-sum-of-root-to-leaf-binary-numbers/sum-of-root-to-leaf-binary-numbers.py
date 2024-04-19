# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        '''
        dfs
        t n 
        s n 
        '''
        def rec(root,num):
            if root == None:
       
                return 0
            if (root.left == None) and (root.right == None):
                print(num*2 + root.val)
                return num*2 + root.val
            
            return rec(root.left,num*2+root.val)+ rec(root.right,num*2+root.val)

        return rec(root,0)