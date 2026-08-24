class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = strs[0]
        for x in range(1, len(strs)):
            iterator = 0
            word = strs[x]
            
            while start and iterator < len(start) and iterator < len(word):
                if start[iterator] != word[iterator]:
                    start = start[0:iterator]
                    continue
                iterator += 1
            start = word[0:iterator]
        return start