from collections import deque as deq
#solution 1 

#bfs traversal on the diagonal
#at each time insert the down cell  and right cell of a visiting cell

'''
t  n  = total cells in grid
s (queue size) max lenght of a diagonal 
'''


'''

solution 2  - using minheap
each diag is characterised by the value i+j
and in each diag we need the cell having lowest col value , 
so we push all these info into minheap and retrieve later 

t  nlogn total cells in grid
s n



solution 3  - using map
key is the diag value i+j and values are teh list of cells in this diag

finally retrieve all of the cells in the grid
while retrivering for a specific i+j diagonal , we need to retrive values from end of the list as the first elemet in the diag
will be last element in the list


t  n =  total cells in grid
s n



'''
#solution1
# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         q = deq([(0,0)])
#         vis = set()
#         vis.add((0,0))
#         ans =[]
#         def out(coord):
#             i,j = coord[0],coord[1]
#             return i<0 or i>=len(nums) or j<0 or j>= len(nums[i])

#         while(q):

#             i,j = q.popleft()

#             ans.append(nums[i][j])
#             down,right = (i+1,j), (i,j+1)

#             if( not out(down)) and( down not in vis):
#                 vis.add(down)
#                 q.append(down)
            
#             if (not out(right)) and (right not in vis):
#                 vis.add(right)
#                 q.append(right)
#         return ans


# #solution 2

# import heapq as h
# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
#         minHeap =[]
#         ans = []
#         for i in range(len(nums)):
#             for j in range(len(nums[i])):
#                 h.heappush(minHeap,(i+j,j,i))


#         while(minHeap):
#             diagVal , j,i = h.heappop(minHeap)
#             ans.append(nums[i][j])
#         return ans

#solution3 
from collections import defaultdict as dict 
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        mp = dict(list)

        for i in range(len(nums)): 
            for j in range(len(nums[i])):

                mp[i+j].append((i,j))
        res =[ ]
        for diagVal in mp:
            for i,j in mp[diagVal][::-1]:
                res.append(nums[i][j])    
        return res    
'''
t n = toal cells in the grid
s n = total cells in the grid

'''

        