class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0,] * len(temperatures)
        
        for x in range(len(temperatures)):
            if stack and temperatures[x] > temperatures[stack[-1]]:
                while stack and temperatures[x] > temperatures[stack[-1]]: 
                    result[stack[-1]] = x - stack[-1]
                    stack.pop()
                stack.append(x)
            else:
                stack.append(x)
            print(stack)
        return result




        