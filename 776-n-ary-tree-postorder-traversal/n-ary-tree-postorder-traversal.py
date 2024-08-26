class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stk = []
        
        if root:
            stk = [root]
        ans  = []
        while(stk):
            root = stk.pop(-1)
            ans.append(root.val)
            for c in root.children:
                stk.append(c)
        return ans[::-1]
