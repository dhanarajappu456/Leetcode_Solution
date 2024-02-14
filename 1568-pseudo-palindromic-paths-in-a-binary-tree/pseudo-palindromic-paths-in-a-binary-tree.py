from collections import defaultdict as dict 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        self.s = set()
        self.ans =0  
        self.li =[]
        def rec(root):
            if root:
                self.li.append(root.val)
                if root.val in self.s:
                    self.s.remove(root.val)
                else:
                    self.s.add(root.val)
           
                if root.left == None and root.right == None:
                    if len(self.s) ==1 or len(self.s)==0: 
                        
                        self.ans+= 1
                    self.li.pop(-1)
                    if root.val in self.s:
                        self.s.remove(root.val)
              
                        
                    return 
                old = self.s.copy()
                rec(root.left)
                self.s = old.copy()
                rec(root.right)
                self.s = old.copy()
                if root.val in self.s:
                    self.s.remove(root.val)
                self.li.pop(-1)

            if root == None:
                # if len(self.s) ==1 or len(self.s)==0: 
                #     print("kfkfk",self.li)
                #     self.ans+= 1        
                return 
            
          
        rec(root)

        return self.ans
        