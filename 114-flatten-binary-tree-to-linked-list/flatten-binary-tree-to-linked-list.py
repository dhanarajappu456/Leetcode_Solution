class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:        
        def rec(root):
            if root  == None:
                return None
            a = rec( root.right)
            b = rec( root.left)
            if b:
              b.right = root.right
            if root.left: 
                root.right = root.left
                root.left = None
            return a or b or   root
        rec(root)
        return root