from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dct={}
        for x in t:
            dct[x]=dct.get(x, 0)+1
        
        i={}
        curr=deque()
        m=""
        y=0
        form=0
        for x in s:
            if x in dct:
                i[x]=i.get(x, 0)+1
                if i[x] == dct[x]:
                     form+=1
            curr.append(x)
            while form == len(dct):
                if not m or len(curr) < len(m):
                    m="".join(curr)
                char_left = curr.popleft()
                if char_left in i:
                    if i[char_left] == dct[char_left]:
                        form-=1
                    i[char_left]-=1
                y+=1
        return m