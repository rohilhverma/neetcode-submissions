class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDct={}
        tDct={}
        if (len(s) != len(t)):
            return False
        for x in range(len(s)):
           sDct[s[x]]=sDct.get(s[x], 1) + 1
           tDct[t[x]]=tDct.get(t[x], 1) + 1
        return sDct == tDct
