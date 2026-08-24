class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l=1

        while l <= r:
            m = (l+r)//2 #current pace of eating bananas
            count = 0

            for x in piles:
                count += math.ceil(x / m) #num of hours to eat everything
            
            if count <= h: #means you're eat too fast. 
                r = m - 1
            else:
                l = m + 1
        
        return l

                