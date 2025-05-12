class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:        
        def rec(root):
            if root  == None:
                return  None
            right_tail= rec( root.right)
            left_tail= rec( root.left)
            if left_tail:
              left_tail.right = root.right
            #make sure to attach the lefr flattened list to the root.right , 
            #iff it is not null ,otherwise it gonna give wrong ans , by attacjing none 
            #to the root.right
            if root.left: 
                root.right = root.left
                root.left  = None
            return right_tail or left_tail or   root
        rec(root)
        return root