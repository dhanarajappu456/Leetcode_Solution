from collections import defaultdict as dict
'''

a binary tree has n-1 edges and n nodes , with no cycle , this also ensures that there exist only one path b/w each pair of vertices 



1)ensuring a single path b/w all pair of vertices  - check if indegree of any node >1, which means it is nor a bin tree
2) count total edges is n-1
3)if all the above is true , check if it has cycle 

if all these is obeyed then  it is a binary tree



'''
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        n = len(leftChild)
        indegree =[0 for i in range(n)]

        adj = dict(list)
        edgeCount  = 0
        #check if indegree  of any node is more than 1 , in which case is not a tree
    
        for i in range(n):
            if leftChild[i]!=-1:
                indegree[leftChild[i]]+=1
                edgeCount+=1
                if indegree[leftChild[i]]>1:
                    return False

            if rightChild[i]!=-1:
                indegree[rightChild[i]]+=1
                edgeCount+=1
                if indegree[rightChild[i]]>1:
                    return False
        
        if edgeCount!=n-1:
            return False

        #if all these true now check if there is cycle - in  case cycle , exits,  it is not truw
        cycle  ={}

        def rec(node):

            if  node  in cycle :
                return cycle[node] 
            cycle[node] = True

            
            l = leftChild[node]
            r = rightChild[node]
            left,right  = False , False
            if l!=-1:
                left = rec(l)
            if r!=-1:
                right  = rec(r)
            cycle[node] =  left or right 
            return cycle[node]
        
        # for i in range(n):
        #     if rec(i):
        #         return False
        # return True

        if rec(0):
            return False
        return True


            


        

        
        

        

        

        