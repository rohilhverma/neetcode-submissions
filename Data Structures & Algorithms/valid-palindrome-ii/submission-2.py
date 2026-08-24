class Solution:
    def validPalindrome(self, s: str) -> bool:
        x, y = 0,len(s)-1
        while x < y:
            if s[x] != s[y]:
                return s[x+1:y+1] == s[x+1:y+1][::-1] or s[x:y] == s[x:y][::-1]
            x += 1
            y -= 1
        return True
        