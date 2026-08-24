class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x=0
        y=len(heights)-1
        vol=0

        while x<y:
            z = (y-x)*min(heights[x], heights[y])
            if z>vol:
                vol=z
            if heights[x] > heights[y]:
                y -= 1
            else:
                x += 1
        
        return vol

