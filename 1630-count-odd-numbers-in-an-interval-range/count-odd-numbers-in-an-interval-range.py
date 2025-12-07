class Solution:
    def countOdds(self, low: int, high: int) -> int:


        #if both end is odd


        if low%2 == 1 and high %2 ==1:
            return math.ceil((high-low+1)/2)

        #if both end is even
        elif low%2 == 1 and high %2 ==1:
            return math.floor((high-low+1)/2)
        #if either end is even 

        else:
            return (high-low+1)//2

        