class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        y=0
        m=0
        for x in range(len(s)):
            if s[x] in hashset:
                while y<x and s[x] in hashset:
                    hashset.remove(s[y])
                    y+=1
            hashset.add(s[x])
            m=max(m,len(hashset))
        return m