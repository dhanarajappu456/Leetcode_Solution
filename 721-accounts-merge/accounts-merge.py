from collections import defaultdict as dict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #create adj list mail mapped to anmother mail(if it belongs to same person )
    #so a component , will be containing all the mail of a same person
          

        processed_mails  =set()
        def dfs(node):
         
            if node in processed_mails:
                return []
            
            mails  =[]
            mails.append(node)
            processed_mails.add(node)
            for neib in adj[node]:

                mails.extend(dfs(neib))
            
        
            return mails

        adj = dict(set)

        
        def createGraph(mails):
            n = len(mails )
            for i in range(n):

                if i>0:
                    adj[mails[i]].add(mails[i-1])
                    adj[mails[i-1]].add(mails[i])
            
            

        for acc in accounts:
            createGraph(acc[1:])
        
        res =[]
        for acc in accounts:
            #if the mail is not processed process that component ,of mails
            if acc[1] not in processed_mails:
                print(acc[1])
                ans= dfs(acc[1])
                ans.sort()
                res.append([acc[0]]+ans)
                

      
        return res

