
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.rec(root,p,q)
          
    def rec(self,root,p,q):
        if root ==None or (root==p) or (root==q):
            return root  
        left =self.rec(root.left,p,q)
        right = self.rec(root.right,p,q)
        
        if left  and right:
            return root
        elif right ==None:
            return left
        else:
            return right
        