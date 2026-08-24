class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=[0]*len(temperatures)
        stack=[]
        
        for x in range(len(temperatures)):
            if stack and temperatures[stack[-1]] < temperatures[x]:
                while stack and temperatures[stack[-1]] < temperatures[x]:
                    z = stack.pop()
                    temp[z] = x - z
            stack.append(x)
        return temp