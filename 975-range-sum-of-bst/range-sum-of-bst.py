'''
use the property of the BST


t  m  = number of  with value in the range
s  m(aux space)





'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans  =0 

        def rec(root):
            nonlocal ans 

            if root ==None:
                return 
            #if node value<low then no need of going left as all nodes in left  subtree of it would be<low 
            if root.val< low :
                rec(root.right)
            #if node value>low then no need of going right as all nodes in right   subtree of it would be>high 
            elif root.val>high:
                rec(root.left)
            #else take current node value and also check left as well as right node(ie preorder of bst , which is giving the result in sorted order)
            else:
            
                ans+=root.val
                

                rec(root.left)
                rec(root.right)
            
        rec(root)
        return ans