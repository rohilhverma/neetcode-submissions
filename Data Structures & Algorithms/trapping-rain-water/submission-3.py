class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,mL,mR,area=0,len(height)-1,height[0],height[-1],0

        while l < r:
            if mL <= mR:   
                l+=1     
                mL=max(mL,height[l])
                if mL-height[l] >0:area+=mL-height[l]
            else:
                r-=1
                mR=max(mR,height[r])
                if mR-height[r]>0:area+=mR-height[r]
        return area
                