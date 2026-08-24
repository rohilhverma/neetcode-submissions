class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        count=max(piles)
        while l<=r:
            mid=(l+r)//2
            rate=0
            for x in piles:
                rate += (x // mid)
                if (x % mid):
                    rate += 1
            if rate > h:
                l=mid+1
            else:
                r=mid-1
                count=min(count, mid)
        return count
            