from collections import defaultdict as dict, deque as dq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList :
            return 0
        adj = dict(list)
        visited  = set()
        for word in wordList:
            
            for ind in range(len(word)):
                pattern  = word[:ind] + "*" +word[ind+1:]
                adj[pattern].append(word)
        
        q= dq([(beginWord,1)])
        visited.add(beginWord)
        while(q):
            
            word,step =q.popleft()
            for ind in range(len(word)):
                pattern = word[:ind] + "*" +word[ind+1:]
                if pattern not in visited:
                    visited.add(pattern)

                    for neib in adj[pattern]:
                            
                            if neib ==endWord:
                                return step+1
                            if neib not in visited:
                                q.append((neib,step+1))
                                visited.add(neib)
                
                        
                            
        return 0