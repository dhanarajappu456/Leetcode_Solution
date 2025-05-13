class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        
        # mp[i] stores how many characters with value (a + i) we have
        mp = [0] * 26
        for c in s:
            mp[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            temp = [0] * 26
            for i in range(26):
                count = mp[i]
                if i == 25:  # 'z'
                    temp[0] = (temp[0] + count) % mod  # 'a'
                    temp[1] = (temp[1] + count) % mod  # 'b'
                else:
                    temp[i + 1] = (temp[i + 1] + count) % mod
            mp = temp
        
        return sum(mp) % mod
