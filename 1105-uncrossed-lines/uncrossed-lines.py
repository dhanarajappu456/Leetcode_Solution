class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
     
        m2 =defaultdict(deque)
        for j in range(len(nums2)) :
            m2[nums2[j]].append(j)

        m,n   = len(nums1) , len( nums2)
        memo  = { }
        def rec(i,j) :

            if i>=m or j>=n :
                return 0 
            if (i,j ) in memo: 
                return memo[(i,j)]
            tk_ = -1
            not_ = -1 
            max_ =  0 
          
            ind1=i
            num = nums1[ind1]
            
                
            ind2 =-1
            if m2[num]:
                
            
                for ind in range(n):

                    if nums2[ind]==num and ind>=j:
                        ind2 = ind
                        break 
            
                            



            if ind2>-1:

                
                tk_ = 1+rec(ind1+1, ind2+1 )
                    
            not_ = rec(ind1+1,j)
     
            memo[(i, j)] = max(max_ , tk_, not_)
            return memo[(i, j)]

        return rec(0, -1)
