class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustors ={i:0 for i in range(1,n+1)}
        trusts_atleast_one =set()
        for rel in trust:
            trustors[rel[1]]+=1
            trusts_atleast_one.add(rel[0])
        for people in trustors:
            if trustors[people] == n-1  and people not in trusts_atleast_one:
                return people
        return -1
        