class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lst=[]
        area=0
        for x in range(len(heights)):
            if lst and heights[x] < lst[-1][0]:
                indx=0
                while lst and heights[x] < lst[-1][0]:
                    temp = lst.pop()
                    area = max(area, (x-temp[1])*temp[0])
                    indx = temp[1]
                if not lst:
                    lst.append((heights[x], 0))
                else:
                    lst.append((heights[x], indx))
            else:
                lst.append((heights[x], x))
            
        for x in lst:
            area = max(area, (len(heights) - x[1]) * x[0])
        return area
        

            