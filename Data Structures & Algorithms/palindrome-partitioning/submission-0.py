class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.lst=[]

        
        def help(indx, lst):
            def pal(s):
                return s == s[::-1]
            if indx == len(s):
                self.lst.append(lst.copy())
                return
            
            for x in range(indx, len(s)):
                if pal(s[indx:x+1]):
                    lst.append(s[indx:x+1])
                    help(x+1, lst)
                    lst.pop()
            
        help(0,[])
        return self.lst