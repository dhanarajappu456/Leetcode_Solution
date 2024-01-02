'''
solution 1
greedy 
we keep a  map with count of each character we fill in current row with each occurence of num in 
map. and this is repeated for each row till map is empty

t n 
s n(the 2d array take space = number of element in the given array)
'''
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        mp ={}
        for num in nums:
            mp[num] = mp.get(num,0)+1
        ans= []
        while mp:
            li =[]
            #iterating on copy to avoid getting error
            #mp modified during iteriton
            for num in mp.copy():
                li.append(num)
                mp[num]-=1
                if mp[num] ==0:
                    mp.pop(num)

            ans.append(li)
    
        return ans 

        