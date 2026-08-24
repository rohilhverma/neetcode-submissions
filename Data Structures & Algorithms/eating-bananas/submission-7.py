class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        m=max(piles)
        while l < r:
            mid = (l+r)//2
            hrs=0
            for x in piles:
                hrs += (x // mid)
                if (x % mid):
                    hrs+=1
            
            if hrs <= h:
                m=min(m, mid)
                r=mid
            else:
                l=mid+1

        return m
