from collections import defaultdict as dict
'''

using the traversal on each of the connected components

the idea is simple. 
we create a component , where all the nodes are the mails belonging to the same person - this adj list created
by the create graph function , thus if 2 accounts have common mail , it would be automatically added to the same component 


then for each account we check if the first mail(if first mail is processed all of the mail in the same account and other mails of the same person  would have been already visitd ), is processed, if not
we visit all the mails of that component and add it as mails of a new person 


'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #create adj list mail mapped to anmother mail(if it belongs to same person )
    #so a component , will be containing all the mail of a same person
          
        #keeps track of visited mail so , that same component(mails of same person ) not visited again
        processed_mails  =set()
        #to traverse a component and get all the mails associated with the same person 
        def dfs(node):
         
            if node in processed_mails:
                return []
            
            mails  =[]
            mails.append(node)
            processed_mails.add(node)
            for neib in adj[node]:
                #we can neglect the extend list time complexity
                mails.extend(dfs(neib))
            
        
            return mails

        adj = dict(set)

        #create adjlist , a component is set of mails belonging to a particular person 
        def createGraph(mails):
            n = len(mails )
            for i in range(n):

                if i>0:
                    adj[mails[i]].add(mails[i-1])
                    adj[mails[i-1]].add(mails[i])
            
            
        #creating the adjlist
        for acc in accounts:
            createGraph(acc[1:])
        
        res =[]
        for acc in accounts:
            #if the mail is not processed process that component ,of mails, for a person
            if acc[1] not in processed_mails:
              
                ans= dfs(acc[1])
                ans.sort()
                res.append([acc[0]]+ans)
                

        return res
        '''
        t  creating adj list n*m (accounts array length , and each account length) = 10^5 + dfs(at worst will travel all mails , once = nm)
        s n +n^2

        '''

