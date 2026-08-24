class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        y,m=0,0
        for x in range(len(s)):
            if s[x] in hashset:
                while y<x and s[x] in hashset:
                    hashset.remove(s[y])
                    y+=1
            hashset.add(s[x])
            m=max(len(hashset),m)
        return m
            
