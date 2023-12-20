'''
just find the 2 min priced choclate and check if you can buy it , successfully with leftove money , 
if yes return remaining money , else dont buy and return what money you have already 

t  n
s  1 

'''



#solution 1
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        

        min_1,min_2 = float(inf), float("inf")
        n = len(prices)

        for i in range(n):

            if prices[i]<=min_1:
                min_2  = min_1
                min_1 = prices[i]
            elif prices[i]<min_2:
                min_2 = prices[i]
            
        left = money-(min_1+min_2)
        if left<0:
            return money
        return left