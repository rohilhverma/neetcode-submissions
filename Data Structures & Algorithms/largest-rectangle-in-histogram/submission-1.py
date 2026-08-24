class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        a = 0
        lst=[]
        for x in range(len(heights)):
            loc=x
            if lst and lst[-1][0] > heights[x]:
                while lst and lst[-1][0] > heights[x]:
                    a = max( (x - lst[-1][1]) * (lst[-1][0]) , a)
                    loc = lst[-1][-1]  
                    lst.pop()
            lst.append((heights[x], loc))    
        
        for x in lst:
            a = max( (len(heights) - x[1]) * x[0] , a)
    
        return a