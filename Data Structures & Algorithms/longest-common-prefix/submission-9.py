class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=min(strs)
        z=s
        for x in strs:
            if s == x:
                continue
            for y in range(len(z)):
                if z[y] != x[y]:
                    z=s[:y]
                    break
        return z