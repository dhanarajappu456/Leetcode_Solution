class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts = defaultdict(int)
        for w in words2:
            curr_cnts = defaultdict(int)
            for c in w:
                curr_cnts[c]+=1
            for c in curr_cnts:
                counts[c] = max(counts[c],curr_cnts[c])
        ans = set(words1)
        for w in words1:
            curr_cnts = Counter(w)
            for c in counts:
                if curr_cnts[c]< counts[c]:
                    ans.remove(w)
                    break
        return list(ans)