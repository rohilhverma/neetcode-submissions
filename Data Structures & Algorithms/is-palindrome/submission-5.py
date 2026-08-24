class Solution:
    def isPalindrome(self, s: str) -> bool:
        string= "".join(s.split())
        string = string.lower()
        a = 0
        b = len(string)-1
        while a < b:
            while a < b and string[a].isalnum() == False:
                a += 1
            while a < b and string[b].isalnum() == False:
                b -= 1
            if string[a] != string[b]:
                return False
            a += 1
            b -= 1
        return True