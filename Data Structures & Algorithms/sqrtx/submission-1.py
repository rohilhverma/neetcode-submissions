class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        val=0
        while l<=r:
            mid=(l+r)//2
            if mid * mid > x:
                r=mid-1
            else:
                val=max(mid,val)
                l=mid+1
        return val

# 1 9 
# 1 4
# 2 4 
# 3 4