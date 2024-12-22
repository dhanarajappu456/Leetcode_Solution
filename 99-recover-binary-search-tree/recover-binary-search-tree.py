# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first,middle,last = None,None, None
        prev  = None
        def rec(root):
            nonlocal first
            nonlocal middle
            nonlocal last
            nonlocal prev
            if root == None:
                return None
            l = rec(root.left)
            if prev and prev.val>root.val:
                if first == None:
                    first = prev
                    middle =  root
                else:
                    last = root
            prev = root

            r =rec(root.right)
            return root

        rec(root)
        if last:
            first.val,last.val = last.val,first.val 
        else:
            print(first,middle)
            first.val,middle.val = middle.val,first.val 

        return root