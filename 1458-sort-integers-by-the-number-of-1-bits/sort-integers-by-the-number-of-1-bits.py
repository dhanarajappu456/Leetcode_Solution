from sortedcontainers import SortedDict as sd


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def num_bits(num):

            cnt = 0
            while(num):
                num =  num &( num-1)
                cnt+=1
            return cnt

        dic = sd()
        arr.sort() 
        for num in arr:
            key = num_bits(num)
            if key not in dic:
                dic[key] = [num] 
            else: 
                dic[key].append(num)  
        res=[ ]
        for item in dic: 
            res.extend(dic[item]) 
        return res