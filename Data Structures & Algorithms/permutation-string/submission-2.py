class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dct={}
        for x in s1:
            dct[x]=dct.get(x,0)+1
        
        l=0
        freq={}
        for x in range(len(s2)):
            if s2[x] in dct:
                freq[s2[x]]=freq.get(s2[x],0)+1
                if freq[s2[x]] > dct[s2[x]]:
                    while freq[s2[x]] > dct[s2[x]]:
                        if s2[l] in freq:    
                            freq[s2[l]] = freq.get(s2[l])-1
                        l+=1
            else:
                freq={}
            
            if dct==freq: return True
        return False

