'''
solution2 - using mono dec stack

 the idea is to build tree with smallest elements first so that the maximum in the tree is minimised
 so we keep on storing the elements to stack if they are decreasing when a value greater than elements in the stack 
 comes we start building tree with those smallest elemnt and then finally build tree with those tree and this greater 
 element

t n 
s  n

'''

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        stk  = [float("inf")]
        res = 0 
        for i,num in enumerate(arr): 
            while(stk and stk[-1]<= num): 
                curr = stk.pop()
                res+= curr* min(stk[-1],num) 
            stk.append(num)
    
        while(len(stk)>2):
            res  = res +  (stk.pop(-1) * stk[-1] )
        return res