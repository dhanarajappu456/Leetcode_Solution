
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        window_sat = sum(customers[0:minutes])
        non_window_sat = 0
        for i in range(minutes,n):
            if grumpy[i] == 0:
                non_window_sat+= customers[i]
      
        ans = non_window_sat +  window_sat 
        i = minutes
        while(i<n ):
            window_sat+= customers[i] - customers[i-minutes]
            if grumpy[i-minutes] ==0:
                non_window_sat+= customers[i-minutes] 
            if grumpy[i] ==0:
                non_window_sat -= customers[i] 
       
            ans = max(ans, window_sat+non_window_sat )
            i+=1
        return ans


        