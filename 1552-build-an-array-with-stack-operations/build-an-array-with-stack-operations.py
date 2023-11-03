class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        p =0 
        ans =[]
        for  i in range(1,n+1):
            if p ==len(target):
                return ans
            if i < target[p]:
                ans.extend(["Push","Pop"])
            else:
                ans.append("Push")
                p+=1
        
        return ans
        