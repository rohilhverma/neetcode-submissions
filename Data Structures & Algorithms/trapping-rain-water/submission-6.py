class Solution:
    def trap(self, height: List[int]) -> int:
        mL,mR=0,0
        l,r=0,len(height)-1
        area=0
        while l < r:
            if mL <= height[l]:
                mL=height[l]                
            if mR <= height[r]:
                mR = height[r]
            x = min(mL, mR)
            if mL < mR:
                area += x - height[l]
                l+=1
            else:
                area += x - height[r]
                r-=1                
        return area
