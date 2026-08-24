class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=sum(weights)
        l=max(weights)
        ret=0
        while l<=r:
            m=(l+r)//2
            i=0
            j=0
            c=1
            while i<len(weights):
                j+=weights[i]
                if m < j:
                    j=weights[i]
                    c+=1
                i+=1
            
            if c <= days:
                ret=m
                r = m-1
            else:
                l=m+1
    
        return ret
