# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.mp  = defaultdict(bool)
        def dfs(root,x):
            if root  == None:
                self.mp[x] = False
                return 
            self.mp[x]   = True
            l  = dfs(root.left, 2*x + 1 )
            r = dfs(root.right,2*x + 2 )
        dfs(root,0)

    def find(self, target: int) -> bool:
        return self.mp[target]
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)