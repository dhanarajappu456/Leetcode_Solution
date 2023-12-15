class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp  = {}
        ans  =""
        possible_dest =set()
        for s,d in paths:

            mp[s]=d
    
            possible_dest.add(d)

        for d in possible_dest:
            if d not in mp:
                return d 
        