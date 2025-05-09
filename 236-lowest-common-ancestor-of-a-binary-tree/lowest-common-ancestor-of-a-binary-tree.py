
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root,p,q):


            if root  == None:
                return None 
            elif root == p: 
                return p
            elif root == q:
                return q
            

            a = rec(root.left,p,q)
            b = rec(root.right,p,q)

            if a and b:
                return root
            return a or b
        return rec(root , p , q)
            


            
        