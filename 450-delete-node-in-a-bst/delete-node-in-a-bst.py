# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def min_val_find(root):
            temp = root
            min_val = float("inf")
            while(temp):
                min_val  = temp.val
                temp  = temp.left
            return min_val

        def rec(root,key):
            if root  == None:
                return None
            if root.val < key:
                root.right  = rec(root.right,key)
            elif root.val > key:
                root.left =  rec(root.left,key)
            else:
                if root.left == None:
                    return root.right
                elif root.right  == None:
                    return root.left
                else:

                    min_val  = min_val_find( root.right )
                    root.val = min_val 
                    root.right  = rec(root.right, min_val)
                
            
            return root




        return rec(root,key)

            
        