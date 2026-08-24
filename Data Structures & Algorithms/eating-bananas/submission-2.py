class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
        final=0
        while l <= r:
            m=(r+l)//2
            pace=0
            for x in piles:
                pace += math.ceil(x/m)
            if pace <= h: # eating at or too fast
                final=m
                r=m-1
            else:
                l=m+1
        return final
