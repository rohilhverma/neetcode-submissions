class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct={}
        y = 0
        m=0
        for x in range(len(s)):
            dct[s[x]]=dct.get(s[x],0)+1
            m=max(dct.values())
            if x-y+1 - m > k:
                dct[s[y]]-=1
                y+=1
            m=x-y+1
        return m

                

