class Solution:
    def trap(self, height: List[int]) -> int:
        boundL, boundR = 0,0
        l, r = 0, len(height)-1
        area = 0
        while l <= r:
            if boundL < boundR:
                if height[l] > boundL:
                    boundL = height[l]
                else:
                    area += boundL - height[l]
                l += 1
            else:
                if height[r] > boundR:
                    boundR = height[r]
                else:
                    area += boundR - height[r]
                r -=1

        return area
