class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
       
        def rec(root):
            if root == None:
                return None
            left = rec(root.left)
            right = rec(root.right)
            root.left = left
            root.right = right
            if root.val in to_delete:
                if left:
                    ans.append(left)
                if right :
                    ans.append(right)
                return None
            else:
                return root
            
        if rec(root):
            ans.append(root)

        return ans
            
        