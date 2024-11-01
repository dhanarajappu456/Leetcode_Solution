class Solution:
    def maxProduct(self, s: str) -> int:
        n= len(s)
        di =dict()
        for i in range(1<<n):
            st =""
            #constructing the string , based on 
            #chars chosen 

            for j in range(n):
                if i&(1<<j)!=0:
                    st = s[-(j+1)]+st
            #store the subsequence 
            #to dict , if is pali          
            if st[::-1]==st:
                di[i] =  len(st)
                
        max_ = -1*float("inf")
        #findind the max product of  length 
        for i in di:
            for j in di:
                if j&i == 0:
                    max_ = max(max_,di[i]*di[j])
        return max_