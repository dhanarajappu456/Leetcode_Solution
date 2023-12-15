class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp  = {}
        ans  =""
        possible_dest =set()
        sources =set()
        for s,d in paths:
            if s in possible_dest:
                possible_dest.remove(s)
            sources.add(s)
            if d not in sources:
                possible_dest.add(d)

        return possible_dest.pop()
        