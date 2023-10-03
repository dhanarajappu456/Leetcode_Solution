class Solution:
    def numIdenticalPairs(self, nums):

        #keeps count of each number 
        count = {}
        res   = 0 
        for i,num in enumerate( nums ):
            cnt = count.get(num,0)
            #when a new occurence of a num , happens , this number can form pair with all the previous
            #occurence of num
            res+= cnt
            cnt+=1 
            count[num] = cnt

        return res 



        #t = n
        #s = n 



        