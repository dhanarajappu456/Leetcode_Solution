#solution - 1
'''
understanding the fact theaty each diagonal is identified by 
 i+j , where i,j is coordiantate of elements in it
 we store these values in map , where key is the diag values
 and values is a dequeue of items of these elements
 dequeue is used , since we need to enque the elements from both side, based 
 on if diag value is odd or even
 t  mn 
 s mn

'''
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         m,n = len(mat),len(mat[0])
#         arr = [ deque([]) for i in range(m+n-1)]
  
#         for i in range(m):
#             for j in range(n):
#                 if (i+j)%2 !=0:
#                     arr[i+j].append(mat[i][j])
#                 else:
#                     arr[i+j].appendleft(mat[i][j])
     
#         ans  = []
#         for a in arr:
           
#             for v in a:
#                 ans.append(v)
#         return ans

#solution - 2

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        ans  = []
        upward  = True
        i,j = 0,0
        print()
        while(i<m and j<n):
            ans.append(mat[i][j])
            #case1 - moving  up
            if upward == True:
                #when reaching upper edge
                if i ==0 and j!=n-1:
                    j+=1
                    upward = False

                #when reaching right edge
                elif j == n-1:
                    i+=1
                    upward =False
                #other case

                else:
                    i-=1
                    j+=1

            #case 2 - moving  down
            else:
                #when reaching bottom edge
                if i ==m-1 and j!=n-1:
                    j+=1
                    upward = True

                #when reaching left edge
                elif j == 0:
                    i+=1
                    upward =True
                #other case
                else:
                    i+=1
                    j-=1
        return ans

  
        