class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        m=0
        hashset=set()
        for x in range(len(s)):
            if s[x] in hashset:
                while l<x and s[x] in hashset:
                    hashset.remove(s[l])
                    l+=1
            hashset.add(s[x])
            m=max(len(hashset),m)
        return m
            

