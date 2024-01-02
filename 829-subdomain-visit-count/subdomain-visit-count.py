from collections import defaultdict as dict 

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans= []
        mp = dict(int)
        for url in cpdomains:
            domains = url.split(".")
            times, dom =domains[0].split(" ")
            times = int(times)
            domains[0] = dom

            for i in range(len(domains)):
                mp[".".join(domains[i:])] += times

            
        for domain in mp:
            ans.append(str(mp[domain] )+" "+domain)
        return ans