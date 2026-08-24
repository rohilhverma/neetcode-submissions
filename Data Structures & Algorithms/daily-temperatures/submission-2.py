class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0,]*len(temperatures)
        stack = []
        for x in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(x)
            elif temperatures[stack[-1]] >= temperatures[x]:
                stack.append(x)
            else:
                while stack and temperatures[x] > temperatures[stack[-1]]:
                    z = stack.pop()
                    lst[z] = x - z
                stack.append(x)                
        return lst
