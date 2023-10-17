from collections import defaultdict as dict

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
                    
                    #print("indegree")
                    return False

            if rightChild[i]!=-1:
                indegree[rightChild[i]]+=1
                edgeCount+=1

                if indegree[rightChild[i]]>1:
                 
                    #print("indegree")
                    return False
        
        if edgeCount!=n-1:
            #print("edge",edgeCount)
            return False

        #if all these true now check if there is cycle


        cycle  ={}

        def rec(node):

            
            if  node  in cycle :
                print("node",node)
                return cycle[node] 
            

            cycle[node] = True

            
            l = leftChild[node]
            r = rightChild[node]
            left,right  = False , False
            if l!=-1:
                
            
                left = rec(l)
            if r!=-1:
                
                right  = rec(r)
            
            
            #print("node",node,left,right)
            cycle[node] =  left or right 

            return cycle[node]
        
        for i in range(n):

            if rec(i):
                #print(i)
                #print(cycle)
                return False
        return True


            


        

        
        

        

        

        