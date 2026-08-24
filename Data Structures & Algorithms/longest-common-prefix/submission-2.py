class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        string = ""
        for x in range(len(first)):
            for y in strs:
                if len(y) == x or first[x] != y[x]:
                    return string
            string += first[x]
        return string
        