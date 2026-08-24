class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        currentMax = 0
        while l < r:
            if ((r - l) * (min(heights[l], heights[r]))) >= currentMax:
                currentMax = (r-l)*(min(heights[l], heights[r]))
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return currentMax