class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = {}
        dct2 = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            dct1[s[x]] = dct1.get(s[x], 0) + 1
            dct2[t[x]] = dct2.get(t[x],0) + 1
        return dct1 == dct2