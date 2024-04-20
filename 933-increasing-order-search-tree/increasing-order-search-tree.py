# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = None
        temp = root
        while(temp):
            new_root  = temp
            temp = temp.left

        
        def reform(root):
            if root == None:
                return None,None

            
            r_left,r_right = reform(root.right)
            l_left,l_right = reform(root.left)
      
            if l_right:
                l_right.right = root
                root.left = None
            root.right = r_left
            return (l_left or root ),(r_right or root)
        l_left,r_right = reform(root)
        return l_left

        