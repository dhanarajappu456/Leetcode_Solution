class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans  = numBottles
        while( numBottles>= numExchange):
            newFree=numBottles//numExchange
            ans+= newFree
            numBottles = numBottles%numExchange + newFree
        return ans