class Solution:
    def encode(self, strs: List[str]) -> str:
        ret=""
        for s in strs:
            ret = ret + str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        x,lst=0,[]
        while x < len(s):
            ret=""
            n=""
            while s[x].isnumeric():
                n+=s[x]
                x+=1
            lst.append(s[x+1:x+1+int(n)])
            x+=1+int(n)
        return lst
    


