class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        dct={}
        window=0
        for x in range(len(s)):
            dct[s[x]] = dct.get(s[x],0)+1
            if dct and (x-l+1) > max(dct.values())+k:
                while (x-l+1) > max(dct.values())+k:
                    dct[s[l]] -=1
                    l+=1
            window=max(window, (x-l+1))
        return window

