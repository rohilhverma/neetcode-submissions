class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct={}
        l=0
        m=0
        for x in range(len(s)):
            dct[s[x]] = dct.get(s[x],0)+1
            if x-l+1 - max(dct.values()) <= k:
                m=max(x-l+1,m)

            else:
                dct[s[l]] -= 1
                l += 1
        return m
            
            
