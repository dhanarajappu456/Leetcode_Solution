# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def count_nodes(root):
            
            if root  == None:
                return 0 
            l_h = find_lheight(root)
            r_h = find_rheight(root)

            if l_h == r_h:
                return 2**l_h - 1
            # if the number left and right height are same then return the number of nodes
            return( 1 + count_nodes(root.left)  +  count_nodes(root.right))
            # if the the left and right height is  not same then call the number of nodes
            # function recursively

        
        def find_lheight(root):
            ht  = 0 
            while(root):
                ht+=1
                root = root.left
            return ht

        def find_rheight(root):
            ht  = 0 
            while(root):
                root = root.right
                ht+=1
            return ht
        
        return count_nodes(root)



                



       
       



        