class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        count=0
        final=sum(weights)
        while l<=r:
            mid=(l+r)//2
            s=0
            x=0
            d=1
            for x in range(len(weights)):
                s += weights[x]
                if s > mid:
                    d+=1
                    s = weights[x]
            if d > days:
                l=mid+1
            else:
                r=mid-1
                final=min(mid,final)
        return final
                


                    
                
                    