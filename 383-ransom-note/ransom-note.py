class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r_mp,m_mp = {},{}


        for i,c in enumerate(ransomNote):
            r_mp[c] = r_mp.get(c,0)+1
        for i ,c in enumerate(magazine):
            m_mp[c] = m_mp.get(c,0)+1

       
        for c in r_mp:

            if m_mp.get(c,0) < r_mp[c]:
                return False
        return True
        