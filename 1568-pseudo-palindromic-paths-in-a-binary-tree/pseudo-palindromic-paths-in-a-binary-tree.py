'''
simple tree dfs traversal

a path can be pali permuated , if even number occurence of all the number and/or  a single number with
just one occurence 


t n 
s h  = (len(set)) + aux space(h) , h can be at max height of the tree  = n 


'''

from collections import defaultdict as dict 

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
        