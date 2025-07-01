import heapq as h 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0 
        #nlogn
        h.heapify(nums)
        while(nums):
            #logn
            mn = h.heappop(nums)
            if mn ==0 :
                continue
            flag = False
            #n
            for i in range(len(nums)):
                if nums[i] != 0:
                    flag  =True
                nums[i] = max(0, nums[i] - mn)
            if flag:
                cnt+=1
            else:
                return cnt+1
        return cnt
        
    '''
    time complexity  is nlogn
    space complexity is n
    '''

