from collections import deque as deq
#solution 1 

#bfs traversal on the diagonal
#at each time insert the down cell  and right cell of a visiting cell

'''
t n  = toal cell in grid
s  n
'''


'''

solution 2  - using minheap
each diag is characterised by the value i+j
and in each diag we need the cell having lowest col value , 
so we push all these info into minheap and retrieve later 

t  n 
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


#solution 2

import heapq as h
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        minHeap =[]
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                h.heappush(minHeap,(i+j,j,i))


        while(minHeap):
            diagVal , j,i = h.heappop(minHeap)
            ans.append(nums[i][j])
        return ans





        

        