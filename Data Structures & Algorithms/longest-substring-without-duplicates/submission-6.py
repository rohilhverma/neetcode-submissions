class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        count=0
        l=0

        for x in range(len(s)):
            if s[x] in hashset:
                while s[x] in hashset:
                    hashset.remove(s[l])
                    l+=1
            hashset.add(s[x])
            count=max(count,len(hashset))
        return count