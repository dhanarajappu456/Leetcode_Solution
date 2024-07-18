# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans   =  0
        def rec(root):


            if root == None:
                return [ ] 
            
            if root.left == None and root.right == None:
                return [1]
            left_leaf_depths = rec (root.left)
            right_leaf_depths = rec (root.right)

            for d1 in left_leaf_depths:
                for d2 in right_leaf_depths:
            
                    if d1+d2  <= distance:

                        self.ans+=1
            all_depths = left_leaf_depths + right_leaf_depths
            return [d+1 for d in all_depths]
        rec(root)
        return self.ans




        