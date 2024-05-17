# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:


        def rec(root):
            if root == None:
                return root
            if (root.left == None)  and (root.right == None):
                if (root.val == target):
                    return None
                return root

            l = rec(root.left)
            r = rec(root.right)
            root.left = l
            root.right = r 
            if (l == None) and( r == None) and (root.val  == target):
                return None
            return root
        return rec(root)
        