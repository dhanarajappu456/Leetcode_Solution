class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        flag  = True
        arr  =[ 0 for i in range(n)]
        for i in range(n-1,-1,-1):
            num  = nums[i]
            mp[num]+=1 
            if flag == False or mp[num]>1:
                flag = False
            arr[i] = flag

        print(arr)

        op = 0 
        for i in range(0,n,3):
            if arr[i] == True:
                return op
            else:
                op+=1
        return op



        
                







            

        




        