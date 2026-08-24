class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        y, l=0,0
        for x in range(len(s)):
            while s[x] in hashset:
                hashset.remove(s[y])
                y += 1
            hashset.add(s[x])
            l = max(l, x-y+1)
        
        return l