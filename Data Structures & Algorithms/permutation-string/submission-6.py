class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        for x in s1:
            d1[x]=d1.get(x,0)+1
        d2={}
        

        for x in range(len(s2)):
            if s2[x] in d1:
                d2[s2[x]]=d2.get(s2[x],0)+1
                y = x+1
                while y < len(s2) and y < x + len(s1) :
                    d2[s2[y]]=d2.get(s2[y],0)+1
                    y+=1
                if d1==d2:
                    return True
                d2={}                
        
        return False

                    

                
