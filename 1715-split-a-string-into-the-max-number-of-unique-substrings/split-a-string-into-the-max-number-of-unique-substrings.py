class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #soluion 1 
        #bruteforce - using recursion
        n = len(s)
        self.ans  = -float("inf")
        li = []
        def rec(i):
           
            if i ==n :

                self.ans =  max(self.ans,  len(li))
                return
           
            for j in range(i,n):
                if s[i:j+1] not in li:
                    li.append(s[i:j+1])
                    rec(j+1)
                    li.pop(-1)


  

        rec(0)
        return self.ans



        