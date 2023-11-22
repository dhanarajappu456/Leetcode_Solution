from collections import deque as deq
#solution bfs traversal on the diagonal
#at each time insert the down cell  and right cell of a visiting cell

'''
t n
s  n
'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deq([(0,0)])
        vis = set()
        vis.add((0,0))
        ans =[]
        def out(coord):
            i,j = coord[0],coord[1]
            return i<0 or i>=len(nums) or j<0 or j>= len(nums[i])

        while(q):

            i,j = q.popleft()

            ans.append(nums[i][j])
            down,right = (i+1,j), (i,j+1)

            if( not out(down)) and( down not in vis):
                vis.add(down)
                q.append(down)
            
            if (not out(right)) and (right not in vis):
                vis.add(right)
                q.append(right)
        return ans
        

        