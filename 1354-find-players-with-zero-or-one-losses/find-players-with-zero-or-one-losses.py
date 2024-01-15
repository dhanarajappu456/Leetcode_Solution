class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        totPlayer =set()
        lost = dict()
        for w,l in matches:
            totPlayer.add(w)
            totPlayer.add(l)
            lost[l] = lost.get(l,0)+1
        totPlayer = sorted(totPlayer)
        ans =[[],[]]
        for pl in totPlayer:

            if pl  not  in lost:
                ans[0].append(pl)
            elif lost[pl] ==1:
                ans[1].append(pl)
        return ans


        