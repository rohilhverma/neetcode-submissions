class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s)-1
        while x < y:
            if s[x].isalnum() == False:
                x += 1
                continue
            if s[y].isalnum() == False:
                y -= 1
                continue
            if s[x].lower() != s[y].lower():
                return False 
            x += 1
            y -= 1
        return True
