class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=sum(weights)
        l=max(weights)
        while l <= r:
            m = (r+l)//2
            count=1
            x=0
            s=0
            while x < len(weights):
                if s + weights[x] > m:
                    count+=1
                    s=weights[x]
                else:
                    s += weights[x]
                x+=1
            
            if count <= days:
                r=m-1
            else:
                l=m+1
            
        return l