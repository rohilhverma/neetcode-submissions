class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict={}
        tDict={}
        for x in s:
            sDict[x] = sDict.get(x, 0) + 1
        for y in t:
            tDict[y] = tDict.get(y, 0) + 1
        return sDict == tDict   
        

        