class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        if len(s) != len(t): return False
        
        for x,y in zip(s,t):
            a[x]=a.get(x,0)+1
            b[y]=b.get(y,0)+1
        return a==b