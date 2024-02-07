class Solution:
    def frequencySort(self, s: str) -> str:
        d =dict()
        for c in s:
            d[c]= d.get(c,0)+1
        cnts =[]
        for c in d:
            cnt = d[c]
            cnts.append((cnt,c))
        cnts.sort()
        ans = []
        for cnt,char in cnts[::-1]:
            ans.append(char*cnt)
        return "".join(ans)

