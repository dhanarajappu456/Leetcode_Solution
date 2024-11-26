class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        champion = { i for i in range(n)}
        for a,b in edges:
            # b can't be the champion
            if b in champion:
                champion.remove(b)
        return  champion.pop() if len(champion ) ==1 else -1 
        



        