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
                return defaultdict() 
            
            if root.left == None and root.right == None:
                depths =      defaultdict(int) 
                depths[1] = 1
                return depths
            left_leaf_depths = rec (root.left)
            right_leaf_depths = rec (root.right)
            '''
            this would now be run in d^2
            '''
            for d1 in left_leaf_depths:
                for d2 in right_leaf_depths:
            
                    if d1+d2  <= distance:

                        self.ans +=  left_leaf_depths[d1] * right_leaf_depths[d2]
            all_depths = defaultdict(int)
            '''
            limiting the dist key to be < distance
            '''
            for d1 in left_leaf_depths:
                if d1+1<=distance:
                    all_depths[d1+1]+= left_leaf_depths[d1]
            for d2 in right_leaf_depths:
                if d2+1<=distance:
                    all_depths[d2+1]+= right_leaf_depths[d2]
           
            return all_depths
        rec(root)
        return self.ans




        