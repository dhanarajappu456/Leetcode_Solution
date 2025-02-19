from collections import deque 

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        li= ["a", "b" , "c"]
        # ans  = []
        # res = ""
        # def rec(s,prev_ind):
        #     print(s,prev_ind)
        #     nonlocal res
        #     if s!="":
        #         ans.append(s)
        #     if len(ans) == k:
        #         if len(ans[k-1]) == n :
        #             res = ans[k-1]
        #             return True
        #         return False
        #     inter = True
        #     for i in range(3):
        #         if prev_ind != i:
        #             inter = rec(s+li[i], i)
        #             if inter  == False:
        #                 return inter
        #     return inter
        # rec("",-1)
        # return res
        q = deque([("", -1)])
        cnt  = 0 
        frontier =  0 
        while(q):
            l = len(q)
            
            for j in range(l):
                a = q.popleft()
                s,prev_ind = a
                cnt+=1
                
                if frontier == n and j+1  == k :
                    return s
                for i in range(3):
                    if i != prev_ind:
                        q.append((s+li[i],i))
            if frontier == n :
                return ""
            frontier+=1
        return ""
                





        