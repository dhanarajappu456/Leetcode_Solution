class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def num_bits(num):

            cnt = 0
            while(num):
                num =  num &( num-1)
                cnt+=1
            return cnt

        
        arr.sort(key = lambda x: (num_bits(x),x))   
        return arr   