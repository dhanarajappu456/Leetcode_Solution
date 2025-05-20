class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        


        #create the flag array , where for each query [a,b]
        ''' 
            we will mark  flag array at index a as -1 and index b+1 as +1 

            then we create a cumulativce sum of this arrat so that all the values
            from the indices a to b will be reduced by -1 now and from indec b+1 its
            effect will be gone as the cum sum from that will be 0


        '''
        n = len(nums)
        flag  = [ 0 for i in range(n)]

        for a,b in queries:
            flag[a] -=1
            if b+1 <n:
                flag[b+1] +=1
        print(flag)

        cumul = [0 for i in range(n)]
        s = 0 
        for i in range(n):
            s+= flag[i]
            cumul[i]+= s
        cnt = 0 
        print(cumul)
        for i in range(n):
            val  = max(0, nums[i] + cumul[i])
            print(val , nums[i] ,  cumul[i])
            if val == 0 :
                cnt+=1
  
        return cnt ==n 
      