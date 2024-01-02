class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        mp ={}
        for num in nums:
            mp[num] = mp.get(num,0)+1
        ans= []
        while mp:
            li =[]
           
            for num in mp.copy():
                li.append(num)
                mp[num]-=1
                if mp[num] ==0:
                    mp.pop(num)

            ans.append(li)
    
        return ans 

        