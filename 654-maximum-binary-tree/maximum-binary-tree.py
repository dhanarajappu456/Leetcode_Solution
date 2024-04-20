# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(i,j):

            if j<i:
                return None
            val  = max(nums[i:j+1])
            node = TreeNode(val)
            ind  = nums.index(val)
            print(ind)
            l =rec(i,ind-1)
            r =rec(ind+1,j)
            node.left =l
            node.right = r 
            return node
        n = len(nums)
        return rec(0,n-1)