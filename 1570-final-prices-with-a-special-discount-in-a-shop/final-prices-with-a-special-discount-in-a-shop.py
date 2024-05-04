class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:



        stk = []
        ans  = [0 for i in range(len(prices))]
        for  i,num in reversed(list(enumerate(prices))):
            while(stk and stk[-1]>num):
                stk.pop(-1)
            ans[i] = num- (stk[-1] if stk else 0 )
            stk.append(num)
        return ans 


        