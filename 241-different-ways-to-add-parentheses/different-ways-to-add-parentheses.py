class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def rec(i,j):
            #print(i,j)
            if expression[i:j+1].isdigit():
                return [int(expression[i:j+1])]
            ans =[]
            for k in range(i,j+1):
            
                if expression[k] in ["*","-","+"]:
                    opr = expression[k]
                    a = rec(i,k-1) 
                    b = rec(k+1,j)
                    for a1 in a:
                        for b1 in b:
                            if opr =="-":
                                ans.append(a1-b1)
                            if opr == "*" :
                                ans.append(a1*b1)
                            if opr == "+" :
                                ans.append(a1+b1)
            return ans 
                
        n = len(expression)
        v = rec(0,n-1)
        print(v)
        return(v)